import socket
from _thread import *
import pickle
import time
from game import Game
from maze import maze

server = "192.168.1.101"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SO_ - socket option
# SOL_ - socket option level
# Sets REUSEADDR (as a socket option) to 1 on socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

# List of sockets for select.select()
sockets_list = [s]
connected = {}                    # id : [conn, p, gameid] id是personal_data的id 
games = {}
maps = {}
idCount = 0                       #client連線人數
id = 0                            #personal_data的id
pair_list = [(0,1),(2,3)]         #配對的順序 兩兩一組
pair = False
data_list = []
game_start = False
previous_time = 0
current_time = 0
game_time = 60*2

def threaded_client(conn, id):
    global connected
    global idCount
    global game_start
    conn.send(str.encode(str("success")))
    while True:
        try:
            data = pickle.loads(conn.recv(2048*2))
            if not data:
                break
            else:
                try:
                    if game_start :
                        p = connected[id][1]
                        gameId = connected[id][2]
                        game = games[gameId]
                        map = maps[gameId]
                except:
                    break
                if data.method == "message":
                    pass
                elif data.method == "get_game":
                    game.players[p] = data.information
                    conn.sendall(pickle.dumps(game))
                elif data.method == "get_map":
                    conn.sendall(pickle.dumps(map))
                elif data.method == "get_game_start":
                    conn.sendall(pickle.dumps(game_start))
                elif data.method == "get_p":
                    conn.sendall(pickle.dumps(p))
        except Exception as e:
            print(e)
            break
    print("Lost connection")
    try:
        del games[gameId]
        del maps[gameId]
        del connected[id]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()
def make_pair(data_list):
    pass
    #return pair_list

def wait_for_connection():
    """
    Wait for connecton from new clients, start new thread once connected
    :return: None
    """
    global idCount
    global id
    while True:
        try:
            conn, addr = s.accept()
            personal_data = pickle.loads(conn.recv(2048*2))
            data_list.append(personal_data)
            print(f"[CONNECTION] {addr} connected to the server at {time.time()}")

            #personal_data[id]
            id = id
            connected[id] = [conn, None, None]
            start_new_thread(threaded_client, (conn, id))
            id += 1
            idCount += 1
        except Exception as e:
            print("[EXCEPTION]", e)
            break
    print("SERVER CRASHED")

start_new_thread(wait_for_connection, ())

#server的主要邏輯
while True:
    try:
        #人數到齊之後開始配對
        if idCount == 4 and game_start == False and pair == False:
            #pair_list = make_pair(data_list)
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
            pair = True
            previous_time = time.time()
        
        
        
    except Exception as e:
            print("[EXCEPTION]", e)
            break
print("SERVER CRASHED")
    