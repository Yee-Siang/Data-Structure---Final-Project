import pygame
def main():
    pygame.init()
    state = 0
    main_surface = pygame.display.set_mode((567, 773))
    initial_pic = pygame.image.load("initial.png")
    signup_pic = pygame.image.load("signup.PNG")
    login_pic = pygame.image.load("login_id.png")
    waiting_pic = pygame.image.load("waiting.PNG")
    font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 50)
    word = ''
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:         
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            posn = event.dict["pos"]
            print(posn)
            if state == 0:
                if (175<=posn[0]<=392) and (520<=posn[1]<=592):
                    state = 1
                elif (175<=posn[0]<=392) and (625<=posn[1]<=695):
                    state = 2
            if(500<=posn[0]<=550) and (13<=posn[1]<=69):
                break
            if state == 2 and (174<=posn[0]<=395 and 625<=posn[1]<=695) and word != '':
                #####重要:這裡產生的資料要拿去Tree裏面做search#####
                passcode = int(word)
                ################################################
                state = 3
        if event.type==pygame.KEYDOWN and state == 2:
            key = event.dict["key"]
            #print(key)
            if len(word) < 7:
                if key == 1073741913:
                    word += '1'
                if key == 1073741914:
                    word += '2'
                if key == 1073741915:
                    word += '3'
                if key == 1073741916:
                    word += '4'
                if key == 1073741917:
                    word += '5'
                if key == 1073741918:
                    word += '6'
                if key == 1073741919:
                    word += '7'
                if key == 1073741920:
                    word += '8'
                if key == 1073741921:
                    word += '9'
                if key == 1073741922:
                    word += '0'
            if key == 8 and word != '':
                word = word[:-1]
        if state == 0:
            main_surface.fill((255,255,255))    
            main_surface.blit(initial_pic, (0,0))
        elif state == 1:
            main_surface.fill((255,255,255))
            main_surface.blit(signup_pic, (0,0))
        elif state == 2:
            id_display = font.render(word,True,(0,0,0))
            
            main_surface.fill((255,255,255))
            main_surface.blit(login_pic, (0,0))
            main_surface.blit(id_display, (120, 525))
        elif state == 3:
            main_surface.fill((255,255,255))
            main_surface.blit(waiting_pic, (0,0))
        pygame.display.flip()
    pygame.quit()
#main()
