import socket
import select
from _thread import *
import pickle
from game import Game
from maze import maze

server = "192.168.1.101"
port = 5555
HEADER_LENGTH = 10
chat = False

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
connected = set()
games = {}
maps = {}
idCount = 0

def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048*2))
            if gameId in games:
                game = games[gameId]
                map = maps[gameId]
                if not data:
                    break
                else:
                    if data.method == "message":
                        pass
                    elif data.method == "get":
                        game.players[p] = data.information
                        conn.sendall(pickle.dumps(game))
                    elif data.method == "get_map":
                        print("fuck you")
                        conn.sendall(pickle.dumps(map))
            else:
                break
        except Exception as e:
            print(e)
            break

    print("Lost connection")
    try:
        del games[gameId]
        del maps[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        maps[gameId] = maze().create()
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1
    
    start_new_thread(threaded_client, (conn, p, gameId))