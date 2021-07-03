class Game:
    def __init__(self, id):
        self.state = "playing_game"
        self.id = id
        self.chatroom = []
        self.players = [None, None]

