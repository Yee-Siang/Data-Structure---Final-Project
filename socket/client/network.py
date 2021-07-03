import socket
import pickle


class Network:
    def __init__(self,personal_data):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.101"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.connect(personal_data)

    def connect(self,personal_data):
        try:
            self.client.connect(self.addr)
            self.client.sendall(pickle.dumps(personal_data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

    def send(self, data):
        try:
            self.client.sendall(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048*4))
        except socket.error as e:
            print(e)
