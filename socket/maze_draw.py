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

def carve_out_maze(win, set):
    for i in range(20+1):
        for j in range(20):
            if ((i-1, j), (i, j)) in sets or i == 0 or i == 20:
                pygame.draw.line(screen, WHITE, [j*20+20, i*20+20], [j*20 + 40, i*20+20])
        if i == 20:
            break      
        for j in range(20):
            if ((i, j-1), (i, j)) in sets or j == 0 and i != 0:
                pygame.draw.line(screen, WHITE, [j*20 + 20, i*20 + 20], [j*20 + 20, i*20 + 40])
    pygame.draw.line(screen,WHITE,(420,20),(420,400))
    pygame.display.update()
        
#carve_out_maze()                   # call build the maze  function

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
