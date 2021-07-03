import pygame
image_1 = pygame.image.load('image/character.png')
image_2=pygame.image.load('image/heart.png')
image_1 = pygame.transform.scale(image_1, (30, 30))
image_2=pygame.transform.scale(image_2,(20,20))
class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1
        self.angle = 0
        self.health=5

    def draw(self, win):
        global image_1
        win.blit(pygame.transform.rotate(image_1, self.angle), (self.x,self.y))
    def draw_heart(self, win,x,y):
        global image_2
        win.blit(pygame.transform.rotate(image_2,0),(x,y))

    def update_attr(self,dic):
        self.x = dic["x"] 
        self.y = dic["y"] 
        self.width = dic["width"] 
        self.height = dic["height"] 
        self.vel = dic["vel"] 
        self.angle = dic["angle"]
        self.health=dic["health"]