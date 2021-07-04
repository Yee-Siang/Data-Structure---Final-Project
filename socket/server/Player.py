class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 2
        self.angle = 0

    def update_attr(self,dic):
        self.x = dic["x"] 
        self.y = dic["y"] 
        self.width = dic["width"] 
        self.height = dic["height"] 
        self.vel = dic["vel"] 
        self.angle = dic["angle"]