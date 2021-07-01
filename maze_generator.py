###################################
# Python maze generator program
# using PyGame for animation
# Davis MT
# Python 3.4
# 10.02.2018
###################################

import pygame
import time
import random
from disjointset import maze

# set up pygame window
WIDTH = 500
HEIGHT = 600
FPS = 30

# Define colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)

# initalise Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()





# build the grid
def build_grid(x, y, w):
    grid=[]
    for i in range(1,21):
        x = 20                                                            # set x coordinate to start position
        y = y + 20                                                        # start a new row
        for j in range(1, 21):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])           # top of cell
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])   # right of cell
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])   # bottom of cell
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])           # left of cell
            grid.append((x,y))                                            # add cell to grid list
            x = x + 20
    pygame.draw.rect(screen,BLUE,[21,21,398,398])
    pygame.display.update()                                                                # move cell to new position




def carve_out_maze():
    m=maze()
    sets=m.create()
    for i in range(20+1):

        for j in range(20):
            if ((i-1, j), (i, j)) in sets or i == 0 or i == 20:
                pygame.draw.line(screen, WHITE, [j*20+20, i*20+20], [j*20 + 40, i*20+20])
                pygame.display.update()
            

        if i == 20:
            break

        for j in range(20):
            if ((i, j-1), (i, j)) in sets or j == 0 and i != 0:
                pygame.draw.line(screen, WHITE, [j*20+20, i*20+20], [j*20 + 20, i*20+40])
                pygame.display.update()
            

        
        



build_grid(40, 0, 20)             # 1st argument = x value, 2nd argument = y value, 3rd argument = width of cell
carve_out_maze()               # call build the maze  function


# ##### pygame loop #######
running = True
while running:
    # keep running at the at the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
