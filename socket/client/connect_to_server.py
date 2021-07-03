import pygame
from network import Network
import math
from Player import Player
from Data import Data
from bullet import bullet


def connect_to_server(personal_data):
    pygame.font.init()

    width = 800
    height = 800
    win = pygame.display.set_mode((width, height))
    cell_width = 37
    cell_height = 37
    wall_verticl=set()
    wall_horizontal=set()
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
    def redrawWindow(win, game, p, p1, p2, map,b1,b2):
        win.fill((128,128,128))
        try:
            p2.update_attr(game.players[1-p])
            b2.update_attr(game.bullet[1-p])
        except:
            pass
        p1.draw(win)
        p2.draw(win)
        if b1.show:###判斷是否blit arrow###
            b1.draw(win)
        if b2.show:
            b2.draw(win)
        for i in range(p1.health):
            p2.draw_heart(win,width-40-i*20,10)
        for i in range(p2.health):
            p1.draw_heart(win,20+i*20,10)
        carve_out_maze(win, map)
        pygame.display.update()

    def if_edge_right(p):###
        for i in wall_verticl:
            if p.x+p.width<i[0][0]+p.vel and p.x+p.width>i[0][0]-p.vel:
                if p.y<i[1][1] and p.y>i[0][1]:
                    return False
                if p.y+p.height<i[1][1] and p.y+p.height>i[0][1]:
                    return False
        if p.x+p.width==(20+1)*cell_width:
            return False
        
        return True
    def if_edge_left(p):
        for i in wall_verticl:
            if p.x<i[0][0]+p.vel and p.x>i[0][0]-p.vel:
                if p.y<i[1][1] and p.y>i[0][1]:
                    return False
                if p.y+p.height<i[1][1] and p.y+p.height>i[0][1]:
                    return False
        if p.x==(1)*cell_width:
            return False
        
        return True
    def if_edge_up(p):
        for i in wall_horizontal:
            if p.y<i[0][1]+p.vel and p.y>i[0][1]-p.vel :
                if p.x<i[1][0] and p.x>i[0][0]:
                    return False
                if p.x+p.width<i[1][0] and p.x+p.width>i[0][0]:
                    return False
        if p.y+p.height==(1)*cell_height:
            return False
        
        return True
    def if_edge_down(p):
        for i in wall_horizontal:
            if p.y+p.height<i[0][1]+p.vel and p.y+p.height>i[0][1]-p.vel:
                if p.x<i[1][0] and p.x>i[0][0]:
                    return False
                if p.x+p.width<i[1][0] and p.x+p.width>i[0][0]:
                    return False
        if p.y+p.height==(20+1)*cell_width:
            return False
        return True
    def if_edge_arrow(b):###判斷arrow有沒有碰到牆###
        x1=(b.x+b.width/2)-b.width/2*math.cos(b.angle*180/math.pi)
        y1=(b.y+b.height/2)-b.width/2*math.sin(b.angle*180/math.pi)
        for i in wall_horizontal:
            if y1<i[0][1]+b.vel and y1>i[0][1]-b.vel:
                if x1<i[1][0] and x1>i[0][0]:
                    return False
        for i in wall_verticl:
            if x1<i[0][0]+b.vel and x1>i[0][0]-b.vel:
                if y1<i[1][1] and y1>i[0][1]:
                    return False
        return True
    def if_user_arrow(p,b):###判斷arrow有沒有碰到player###
        xb=(b.x+b.width/2)-b.width/2*math.cos(b.angle*180/math.pi)
        yb=(b.y+b.height/2)-b.width/2*math.sin(b.angle*180/math.pi)
        if xb<p.x+p.width and xb>p.x:
            if yb<p.y+p.height and yb>p.y:
                return True
        return False
    ###

    def play_game():

        play = True
        try:
            #拿到player號碼
            data = Data("get_p",None,None)
            player = n.send(data)
            print("You are player", player)

            #拿到地圖
            data = Data("get_map",None,None)
            map = n.send(data)

            if player == 0:# 我是player1
                p1 = Player(cell_width, cell_height, 30,30)
                p2 = Player(20*cell_width, 20*cell_height, 30,30)
                bullet1=bullet(0,0,30,5)
                bullet2=bullet(0,0,30,5)
            else:          # 我是player2
                p1 = Player(20*cell_width, 20*cell_height, 30,30)
                p2 = Player(cell_width, cell_height, 30,30)
                bullet1=bullet(0,0,30,5)
                bullet2=bullet(0,0,30,5)
        except Exception as e:
            print(e)
            play = False

        while play:
            #更新畫面
            try:
                #拿到遊戲
                data = Data("get_game",p1,bullet1)
                game = n.send(data)

                state = game.state
                if state == "wait_for_pair":
                    play = False
            except Exception as e:
                print(e)
                play = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

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
            if keys[pygame.K_e]:###arrow
                bullet1.x=p1.x
                bullet1.y=p1.y
                bullet1.angle=p1.angle
                bullet1.show=True
            if if_edge_arrow(bullet1) and bullet1.show:
                bullet1.x+=bullet1.vel*math.cos(-bullet1.angle/180*math.pi)
                bullet1.y+=bullet1.vel*math.sin(-bullet1.angle/180*math.pi)
                if if_user_arrow(p2,bullet1) and bullet1.show:
                    p1.health=p1.health-1
                    bullet1.show=False
            else:
                bullet1.show=False
            if p1.health==0:
                 play=False
            redrawWindow(win, game, player, p1, p2, map,bullet1,bullet2)
        while p1.health==0 and play==False:
            myfont = pygame.font.Font(None,60)
            textImage = myfont.render("game over", True, 0,0,200)
            win.blit(textImage, (100,100))
            pygame.display.update()
    
    #connect_to_server
    run = True
    clock = pygame.time.Clock()
    n = Network(personal_data)
    playing = False

    #client問server遊戲開始了沒
    while True :
        clock.tick(60)
        try:
            data = Data("get_client_state",None)
            reply = n.send(data)
            if reply == "playing" :
                #遊戲開始了
                play_game()
            elif reply == "wait_for_pair":
                #等待配對
                win.fill((128,128,128))
                font = pygame.font.SysFont("comicsans", 80)
                text = font.render("Waiting for Pair...", 1, (255,0,0), True)
                win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
            else:
                #不知道甚麼bug
                pygame.quit()
                n.client.close()
                break
        except Exception as e:
            print(e)
            pygame.quit()
            n.client.close()
            break 

if __name__  == '__main__':
    personal_data = input("請輸入您的id:")
    personal_data = {"id":int(personal_data)}
    connect_to_server(personal_data)

