import pygame
from user_and_pair import *
from connect_to_server import connect_to_server

def main():
    pygame.init()
    state = 0
    main_surface = pygame.display.set_mode((567, 773))
    font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 50)
    initial_pic = pygame.image.load("pictures/initial.png")
    signup_pic = pygame.image.load("pictures/signup.PNG")
    login_pic = pygame.image.load("pictures/login_id.png")
    waiting_pic = pygame.image.load("pictures/waiting.PNG")
    male_pic = pygame.image.load("pictures/male.png")
    female_pic = pygame.image.load("pictures/female.png")
    sports_pic = pygame.image.load("pictures/sports.png")
    read_pic = pygame.image.load("pictures/read.png")
    dance_pic = pygame.image.load("pictures/dance.png")
    travel_pic = pygame.image.load("pictures/travel.png")
    write_pic = pygame.image.load("pictures/write.png")
    draw_pic = pygame.image.load("pictures/draw.png")
    movie_pic = pygame.image.load("pictures/movie.png")
    music_pic = pygame.image.load("pictures/music.png")
    game_pic = pygame.image.load("pictures/game.png")
    sign_up_pic = pygame.image.load("pictures/sign_up.png")
    register_success_pic = pygame.image.load("pictures/register_success.png")
    word = ''
    name = ''
    age = ''
    gender = ''
    interest = []
    ideal_age = ''
    ideal_gender = ''
    progress = 0

    personal_data = None

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            posn = event.dict["pos"]
           # print(posn)
            if state == 0:
                if (175 <= posn[0] <= 392) and (520 <= posn[1] <= 592):
                    state = 1
                elif (175 <= posn[0] <= 392) and (625 <= posn[1] <= 695):
                    state = 2
            if(500 <= posn[0] <= 550) and (13 <= posn[1] <= 69) and state != 1:
                break
            if state == 2 and (174 <= posn[0] <= 395 and 625 <= posn[1] <= 695) and word != '':
                #####重要:這裡產生的資料要拿去Tree裏面做search#####
                passcode = int(word)
                personal_data = {}
                personal_data["method"] = "passcode"
                personal_data["information"] = passcode
                ################################################
                state = 3
        if event.type == pygame.KEYDOWN and state == 2:
            key = event.dict["key"]
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
            if key == 1073741904:
                state = 0
            if key == 8 and word != '':
                word = word[:-1]
        if state == 1:
            if event.type == pygame.KEYDOWN:
                key = event.dict["key"]
                # print(key)
                if progress == 0:
                    if 97 <= key <= 122:
                        if chr(key).isalpha() and len(name) < 10:
                            name += chr(key)
                    if len(name) > 0:
                        if key == 13:
                            progress += 1
                        elif key == 8:
                            name = name[:-1]
                if progress == 1:
                    if 1073741913 <= key <= 1073741922 and len(age) < 3:
                        age += str(divmod(key-2, 10)[1])
                    if len(age) > 0:
                        if key == 13:
                            progress += 1
                        elif key == 8:
                            age = age[:-1]
            if event.type == pygame.MOUSEBUTTONDOWN and progress == 2:
                posn = event.dict["pos"]
                # print(posn)
                if (224 <= posn[0] <= 326) and (191 <= posn[1] <= 245):
                    gender = 'male'
                elif (344 <= posn[0] <= 458) and (191 <= posn[1] <= 245):
                    gender = 'female'
            if event.type == pygame.KEYDOWN and progress == 2 and gender != '':
                key = event.dict["key"]
                if key == 13:
                    progress += 1
            if progress == 3:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posn = event.dict["pos"]
                   # print(posn)
                    if (40 <= posn[0] <= 142) and (301 <= posn[1] <= 301+54):
                        if not 'sports' in interest and len(interest) < 3:
                            interest.append('sports')
                        elif 'sports' in interest:
                            interest.remove('sports')
                    elif (40 <= posn[0] <= 142) and (372 <= posn[1] <= 372+54):
                        if not 'read' in interest and len(interest) < 3:
                            interest.append('read')
                        elif 'read' in interest:
                            interest.remove('read')
                    elif (40 <= posn[0] <= 142) and (443 <= posn[1] <= 443+54):
                        if not 'dance' in interest and len(interest) < 3:
                            interest.append('dance')
                        elif 'dance' in interest:
                            interest.remove('dance')
                    elif (186 <= posn[0] <= 186+102) and (301 <= posn[1] <= 355):
                        if not 'travel' in interest and len(interest) < 3:
                            interest.append('travel')
                        elif 'travel' in interest:
                            interest.remove('travel')
                    elif (186 <= posn[0] <= 186+102) and (372 <= posn[1] <= 372+54):
                        if not 'write' in interest and len(interest) < 3:
                            interest.append('write')
                        elif 'write' in interest:
                            interest.remove('write')
                    elif (186 <= posn[0] <= 186+102) and (443 <= posn[1] <= 443+54):
                        if not 'draw' in interest and len(interest) < 3:
                            interest.append('draw')
                        elif 'draw' in interest:
                            interest.remove('draw')
                    elif (332 <= posn[0] <= 332+102) and (301 <= posn[1] <= 355):
                        if not 'movie' in interest and len(interest) < 3:
                            interest.append('movie')
                        elif 'movie' in interest:
                            interest.remove('movie')
                    elif (332 <= posn[0] <= 332+102) and (372 <= posn[1] <= 372+54):
                        if not 'music' in interest and len(interest) < 3:
                            interest.append('music')
                        elif 'music' in interest:
                            interest.remove('music')
                    elif (332 <= posn[0] <= 332+102) and (443 <= posn[1] <= 443+54):
                        if not 'game' in interest and len(interest) < 3:
                            interest.append('game')
                        elif 'game' in interest:
                            interest.remove('game')
                if event.type == pygame.KEYDOWN:
                    key = event.dict["key"]
                    if key == 13 and len(interest) == 3:
                        progress += 1

            if progress == 4:
                if event.type == pygame.KEYDOWN:
                    key = event.dict["key"]
                    if 1073741913 <= key <= 1073741922 and len(ideal_age) < 3:
                        ideal_age += str(divmod(key-2, 10)[1])
                    if len(ideal_age) > 0:
                        if key == 13:
                            progress += 1
                        elif key == 8:
                            ideal_age = ideal_age[:-1]
            if progress == 5:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posn = event.dict["pos"]
                    if (48 <= posn[0] <= 154) and (655 <= posn[1] <= 711):
                        ideal_gender = 'male'
                    elif (172 <= posn[0] <= 172+106) and (655 <= posn[1] <= 711):
                        ideal_gender = 'female'
                if event.type == pygame.KEYDOWN and ideal_gender != '':
                    key = event.dict["key"]
                    if key == 13:
                        progress += 1
            if progress == 6:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posn = event.dict["pos"]
                    if (402 <= posn[0] <= 531) and (654 <= posn[1] <= 714):
                        #####重要:這些產生的資料將來要拿去class裏面做新的user#####
                        new_user = user(name, int(age), gender, interest, int(
                            ideal_age), ideal_gender)
                        personal_data = {}
                        personal_data["method"] = "new_user"
                        personal_data["information"] = new_user

                        state = 4
                    ################################################
        if state == 4:
            if event.type == pygame.MOUSEBUTTONDOWN:
                posn = event.dict["pos"]
                if (216 <= posn[0] <= 330) and (644 <= posn[1] <= 704):
                    state = 3
        if state == 0:
            main_surface.fill((255, 255, 255))
            main_surface.blit(initial_pic, (0, 0))
        elif state == 1:
            name_display = font.render(name, True, (0, 0, 0))
            age_display = font.render(age, True, (0, 0, 0))
            ideal_age_display = font.render(ideal_age, True, (0, 0, 0))
            main_surface.fill((255, 255, 255))
            main_surface.blit(signup_pic, (0, 0))
            if gender == 'male':
                main_surface.blit(male_pic, (212, 185))
            elif gender == 'female':
                main_surface.blit(female_pic, (342, 185))
            if ideal_gender == 'male':
                main_surface.blit(male_pic, (44, 652))
            elif ideal_gender == 'female':
                main_surface.blit(female_pic, (171, 652))
            if 'sports' in interest:
                main_surface.blit(sports_pic, (38, 298))
            if 'read' in interest:
                main_surface.blit(read_pic, (38, 370))
            if 'dance' in interest:
                main_surface.blit(dance_pic, (37, 442))
            if 'travel' in interest:
                main_surface.blit(travel_pic, (183, 298))
            if 'write' in interest:
                main_surface.blit(write_pic, (183, 370))
            if 'draw' in interest:
                main_surface.blit(draw_pic, (183, 443))
            if 'movie' in interest:
                main_surface.blit(movie_pic, (324, 298))
            if 'music' in interest:
                main_surface.blit(music_pic, (324, 370))
            if 'game' in interest:
                main_surface.blit(game_pic, (323, 441))
            if progress == 6:
                main_surface.blit(sign_up_pic, (400, 652))

            main_surface.blit(name_display, (210, 56))
            main_surface.blit(age_display, (164, 122))
            main_surface.blit(ideal_age_display, (273, 538))
        elif state == 2:
            id_display = font.render(word, True, (0, 0, 0))

            main_surface.fill((255, 255, 255))
            main_surface.blit(login_pic, (0, 0))
            main_surface.blit(id_display, (120, 525))
        elif state == 3:
            '''
            main_surface.fill((255, 255, 255))
            main_surface.blit(waiting_pic, (0, 0))
            '''
            main_surface.fill((0, 0, 0))
            pygame.display.flip()
            break
        elif state == 4:
            main_surface.fill((255, 255, 255))
            main_surface.blit(register_success_pic, (0, 0))
            new_id_display = font.render(str(new_user.id), True, (0, 0, 0))
            main_surface.blit(new_id_display, (250, 465))
        pygame.display.flip()
    #pygame.quit()
    return personal_data

personal_data = main()
if personal_data:
    connect_to_server(personal_data)

