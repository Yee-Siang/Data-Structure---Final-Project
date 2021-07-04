import socket
from _thread import *
import pickle
import time
from game import Game
from maze import maze

server = "192.168.1.101"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

# List of sockets for select.select()
sockets_list = [s]
connected = {}                    # id : [conn, p, gameid] id是personal_data的id 
games = {}                        #正在進行的遊戲
maps = {}                         #遊戲的地圖
idCount = 0                       #client連線人數
data_dic = {}                     #在線成員的資料
game_start = False                #統一進行遊戲
game_start_time = 0
current_time = 0
game_time = 30                     #遊戲進行的時間
state = "wait_for_pair"           #server目前的狀態

def threaded_client(conn, id):
    global connected
    global idCount
    global game_start
    global data_dic
    running = game_start
    client_state = "wait_for_pair"
    conn.send(str.encode(str("success")))
    while True:
        try:
            data = pickle.loads(conn.recv(2048*2))
            if not data:
                break
            else:
                try:
                    if game_start and client_state != "game_over" :
                        #所有人正在玩遊戲
                        p = connected[id][1]
                        gameId = connected[id][2]
                        game = games[gameId]
                        map = maps[gameId]
                        client_state = "playing"
                    elif not game_start:
                        client_state = "wait_for_pair"
                except:
                    if game_start :
                        #我的隊友斷線了
                        client_state = "wait_for_pair"

                if data.method == "message":
                    pass
                elif data.method == "get_game":
                    game.players[p] = data.information[0]
                    game.bullet[p] = data.information[1]###
                    game.state = client_state
                    conn.sendall(pickle.dumps(game))
                elif data.method == "get_map":
                    conn.sendall(pickle.dumps(map))
                elif data.method == "get_client_state":
                    conn.sendall(pickle.dumps(client_state))
                elif data.method == "get_p":
                    conn.sendall(pickle.dumps(p))
                elif data.method == "game_over":
                    client_state = "game_over"
                    game.over = True
                    conn.sendall(pickle.dumps(client_state))
                    
        except Exception as e:
            print(e)
            break
    print("Lost connection")
    try:
        del connected[id]
        del data_dic[id]
        del games[gameId]
        del maps[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()
def make_pair(data_dic):
    pair_list = []
    value_list = list(data_dic.values())
    for i in range(0,len(value_list),2):
        pair_tup = (value_list[i]["id"],value_list[i+1]["id"])
        pair_list.append(pair_tup)

    return pair_list

def wait_for_connection():
    """
    Wait for connecton from new clients, start new thread once connected
    :return: None
    """
    global idCount
    while True:
        try:
            conn, addr = s.accept()
            personal_data = pickle.loads(conn.recv(2048*2))
            print(f"[CONNECTION] {addr} connected to the server at {time.time()}")

            id = personal_data["id"]
            data_dic[id] = personal_data
            connected[id] = [conn, None, None]
            start_new_thread(threaded_client, (conn, id))
            idCount += 1
        except Exception as e:
            print("[EXCEPTION]", e)
            break
    print("SERVER CRASHED")

start_new_thread(wait_for_connection, ())

#server的主要邏輯
while True:

    try:
        #人數到齊之後開始重新配對
        if idCount == 2 and game_start == False :
            pair_list = make_pair(data_dic)
            for i in range(len(pair_list)):
                p1_id = pair_list[i][0]
                p2_id = pair_list[i][1]

                games[i] = Game(i)
                maps[i] = maze().create()
                print("Creating a new game...")

                connected[p1_id][1] = 0
                connected[p1_id][2] = i
                connected[p2_id][1] = 1
                connected[p2_id][2] = i
            game_start = True
            game_start_time = time.time()
            state = "playing_game"


        current_time = time.time()
        pass_time = current_time - game_start_time
        #print("在線人數:",idCount)
        if pass_time >= game_time and game_start:
            #遊戲時間結束
            state = "wait_for_pair"
            game_start = False
        

    except Exception as e:
            print("[EXCEPTION]", e)
            break
print("SERVER CRASHED")
    

