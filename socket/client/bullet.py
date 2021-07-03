import pygame
image_3 = pygame.image.load('image/arrow.png')
image_3 = pygame.transform.scale(image_3, (30, 30))
class bullet(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 2
        self.angle = 0
        self.show=False

    def draw(self, win):
        global image_3
        win.blit(pygame.transform.rotate(image_3, self.angle), (self.x,self.y))
    def update_attr(self,dic):
        self.x = dic["x"] 
        self.y = dic["y"] 
        self.width = dic["width"] 
        self.height = dic["height"] 
        self.vel = dic["vel"] 
        self.angle = dic["angle"] 
        self.show=dic["show"]
