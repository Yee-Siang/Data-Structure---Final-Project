class Game:
    def __init__(self, id):
        self.ready = False
        self.id = id
        self.chatroom = []
        self.players = [None, None]

    def connected(self):
        return self.ready

