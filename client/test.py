from connect_to_server import connect_to_server
import threading
while True:
    threading._start_new_thread(connect_to_server, ({"id":456},))
    print("fuck")
#connect_to_server({"id":456})