import pygame
image_1 = pygame.image.load('image/character.png')
image_1 = pygame.transform.scale(image_1, (64, 64))
class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.angle = 0

    def draw(self, win):
        global image_1

        win.blit(pygame.transform.rotate(image_1, self.angle), (self.x,self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
    def update_attr(self,dic):
        self.x = dic["x"] 
        self.y = dic["y"] 
        self.width = dic["width"] 
        self.height = dic["height"] 
        self.vel = dic["vel"]
        self.hitbox = dic["hitbox"] 
        self.angle = dic["angle"]