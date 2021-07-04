import pygame
from network import Network
import pickle
import math
from Player import Player
from Data import Data
pygame.font.init()

width = 800
height = 800
win = pygame.display.set_mode((width, height))
cell_width = 37
cell_height = 37
horizontal_boundary = []
vertical_boundary = []
wall_horizontal=set()
wall_verticl=set()
interval=0
pygame.display.set_caption("Client")

def carve_out_maze(win, sets):
    global cell_width
    global cell_height

    for i in range(20+1):
        for j in range(20):
            if ((i-1, j), (i, j)) in sets or i == 0 or i == 20:
                pygame.draw.line(win, (255, 255, 255), [(j+1)*cell_width, (i+1)*cell_height], [(j+2)*cell_width, (i+1)*cell_height])
                wall_horizontal.add((((j+1)*cell_width, (i+1)*cell_height), ((j+2)*cell_width, (i+1)*cell_height)))
        if i == 20:
            break      
        for j in range(20):
            if ((i, j-1), (i, j)) in sets or j == 0 and i != 0:
                pygame.draw.line(win, (255, 255, 255), [(j+1)*cell_width, (i+1)*cell_height], [(j+1)*cell_width, (i+2)*cell_height])
                wall_verticl.add((((j+1)*cell_width, (i+1)*cell_height), ((j+1)*cell_width, (i+2)*cell_height)))
    pygame.draw.line(win,(255, 255, 255),((20+1)*cell_width,cell_height),((20+1)*cell_width,20*cell_height))
    pygame.display.update()

def redrawWindow(win, game, p, p1, p2, map):
    win.fill((128,128,128))
    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        try:
            p2.update_attr(game.players[1-p])
        except:
            pass
        p1.draw(win)
        p2.draw(win)
        carve_out_maze(win, map)
    pygame.display.update()

def if_edge_right(p):
    for i in wall_verticl:
        if p.x+p.width==i[0][0]:
            if p.y<i[1][1] and p.y>i[0][1]:
                return False
            if p.y+p.height<i[1][1] and p.y+p.height>i[0][1]:
                return False
    print(p.x)
    if p.x+p.width==(20+1)*cell_width:
        print(1)
        return False
    
    return True
def if_edge_left(p):
    for i in wall_verticl:
        if p.x==i[0][0]:
            if p.y<i[1][1] and p.y>i[0][1]:
                return False
            if p.y+p.height<i[1][1] and p.y+p.height>i[0][1]:
                return False
    print(p.x)
    if p.x==(1)*cell_width:
        print(1)
        return False
    
    return True
def if_edge_up(p):
    for i in wall_horizontal:
        if p.y==i[0][1] :
            if p.x<i[1][0] and p.x>i[0][0]:
                return False
            if p.x+p.width<i[1][0] and p.x+p.width>i[0][0]:
                return False
    if p.y+p.height==(1)*cell_height:
        return False
    
    return True
def if_edge_down(p):
    for i in wall_horizontal:
        if p.y+p.height==i[0][1]:
            if p.x<i[1][0] and p.x>i[0][0]:
                return False
            if p.x+p.width<i[1][0] and p.x+p.width>i[0][0]:
                return False
    if p.y+p.height==(20+1)*cell_width:
        return False
    return True
def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player)
    data = Data("get_map",None)
    map = n.send(data)
    
    if player == 0:# 我是player1
        p1 = Player(cell_width, cell_height, 30,30)
        p2 = Player(20*cell_width, 20*cell_height, 30,30)
    else:          # 我是player2
        p1 = Player(20*cell_width, 20*cell_height, 30,30)
        p2 = Player(cell_width, cell_height, 30,30)

    while run:
        clock.tick(60)
        try:
            data = Data("get",p1)
            game = n.send(data)
        except Exception as e:
            run = False
            print("Couldn't get game")
            print(e)
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        #game1 character
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and p1.x > p1.vel and if_edge_left(p1):
            p1.x -= p1.vel
        elif keys[pygame.K_d] and p1.x < width - p1.width - p1.vel and if_edge_right(p1):
            p1.x += p1.vel
        elif keys[pygame.K_w] and p1.y > p1.vel and if_edge_up(p1):
            p1.y -= p1.vel
        elif keys[pygame.K_s] and p1.y < height - p1.width - p1.vel and if_edge_down(p1):
            p1.y += p1.vel
        pos = pygame.mouse.get_pos()
        dx = pos[0] - (p1.x+p1.width)
        dy = pos[1] - (p1.y+p1.height)
        p1.angle = math.atan2(-dy,dx)*180/math.pi
        redrawWindow(win, game, player, p1, p2, map)

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255,0,0))
        win.blit(text, (100,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu_screen()
