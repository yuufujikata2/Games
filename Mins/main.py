import pygame
from pygame.locals import *
import random
import sys

def main():
    pygame.init()
    screen=pygame.display.set_mode((1000,1000))
    pygame.display.set_caption("Minesweeper")
    font = pygame.font.Font(None,80)
    font2 = pygame.font.Font(None,300)
    font3 = pygame.font.Font(None,200)
    clock = pygame.time.Clock()
    hairetu = [[0 for i in range(12)] for j in range(12)]
    for i in range(12):
        hairetu[i][0] = -1
        hairetu[i][11] = -1
        hairetu[0][i] = -1
        hairetu[11][i] = -1
    start_x = None
    start_y = None
    atack_x = None
    atack_y = None
    hantei = None
    mouse_x = None
    mouse_y = None
    clear_chek = None
    restart = None
    flag = None
    flag_x = None
    flag_y = None

    while True :
        while True:     
            clock.tick(40)
            screen.fill((250,250,250))
            for i in range(1,11):
                for j in range(1,11):
                    pygame.draw.rect(screen,(100,100,100),Rect(100 * (i-1), 100 * (j-1),100,100))
                    pygame.draw.rect(screen,(0,0,0),Rect(100 * (i-1), 100 * (j-1),100,100),2)
             
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                """    
                if event.type == KEYDOWN:
                    if event.key == K_0:
                        if start_x == None:
                            start_x = 0
                        elif start_y == None:
                            start_y = 0
                    if event.key == K_1:
                        if start_x == None:
                            start_x = 1
                        elif start_y == None:
                            start_y = 1
                    if event.key == K_2:
                        if start_x == None:
                            start_x = 2
                        elif start_y == None:
                            start_y = 2
                    if event.key == K_3:
                        if start_x == None:
                            start_x = 3
                        elif start_y == None:
                            start_y = 3
                    if event.key == K_4:
                        if start_x == None:
                            start_x = 4
                        elif start_y == None:
                            start_y = 4
                    if event.key == K_5:
                        if start_x == None:
                            start_x = 5
                        elif start_y == None:
                            start_y = 5
                    if event.key == K_6:
                        if start_x == None:
                            start_x = 6
                        elif start_y == None:
                            start_y = 6
                    if event.key == K_7:
                        if start_x == None:
                            start_x = 7
                        elif start_y == None:
                            start_y = 7
                    if event.key == K_8:
                        if start_x == None:
                            start_x = 8
                        elif start_y == None:
                            start_y = 8
                    if event.key == K_9:
                        if start_x == None:
                            start_x = 9
                        elif start_y == None:
                            start_y = 9
                """
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        mouse_x,mouse_y = event.pos
            if mouse_x != None and mouse_y != None:
                if mouse_x > 0 and mouse_x <= 100:
                    start_x = 0
                elif  mouse_x <= 200:
                    start_x = 1
                elif  mouse_x <= 300:
                    start_x = 2
                elif  mouse_x <= 400:
                    start_x = 3
                elif  mouse_x <= 500:
                    start_x = 4
                elif  mouse_x <= 600:
                    start_x = 5
                elif  mouse_x <= 700:
                    start_x = 6
                elif  mouse_x <= 800:
                    start_x = 7
                elif  mouse_x <= 900:
                    start_x = 8
                elif  mouse_x <= 1000:
                    start_x = 9
                if mouse_y > 0 and mouse_y <= 100:
                    start_y = 0
                elif  mouse_y <= 200:
                    start_y = 1
                elif  mouse_y <= 300:
                    start_y = 2
                elif  mouse_y <= 400:
                    start_y = 3
                elif  mouse_y <= 500:
                    start_y = 4
                elif  mouse_y <= 600:
                    start_y = 5
                elif  mouse_y <= 700:
                    start_y = 6
                elif  mouse_y <= 800:
                    start_y = 7
                elif  mouse_y <= 900:
                    start_y = 8
                elif  mouse_y <= 1000:
                    start_y = 9
                mouse_x = None
                mouse_y = None
            if start_y != None and start_y != None:
                bakudanhaichi(start_x+1,start_y+1,hairetu)
                atack_x = start_x
                atack_y = start_y
                break
            pygame.display.update()
        while True:     
            clock.tick(40)
            screen.fill((250,250,250))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_f:
                        if flag :
                            flag = False
                        else:
                            flag = True
#            for i in range(10):
#                for j in range(10):
#                    if hairetu[i][j] ==10:
#                        pygame.draw.circle(screen,(250,0,0),(50 + 100 * i, 50 + 100 * j),40)
                """
                if event.type == KEYDOWN:
                    if event.key == K_0:
                        if atack_x == None:
                            atack_x = 0
                        elif atack_y == None:
                            atack_y = 0
                    if event.key == K_1:
                        if atack_x == None:
                            atack_x = 1
                        elif atack_y == None:
                            atack_y = 1
                    if event.key == K_2:
                        if atack_x == None:
                            atack_x = 2
                        elif atack_y == None:
                            atack_y = 2
                    if event.key == K_3:
                        if atack_x == None:
                            atack_x = 3
                        elif atack_y == None:
                            atack_y = 3
                    if event.key == K_4:
                        if atack_x == None:
                            atack_x = 4
                        elif atack_y == None:
                            atack_y = 4
                    if event.key == K_5:
                        if atack_x == None:
                            atack_x = 5
                        elif atack_y == None:
                            atack_y = 5
                    if event.key == K_6:
                        if atack_x == None:
                            atack_x = 6
                        elif atack_y == None:
                            atack_y = 6
                    if event.key == K_7:
                        if atack_x == None:
                            atack_x = 7
                        elif atack_y == None:
                            atack_y = 7
                    if event.key == K_8:
                        if atack_x == None:
                            atack_x = 8
                        elif atack_y == None:
                            atack_y = 8
                    if event.key == K_9:
                        if atack_x == None:
                            atack_x = 9
                        elif atack_y == None:
                            atack_y = 9
                """
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x,mouse_y = event.pos
            if flag :
                if mouse_x != None and mouse_y != None:
                    if mouse_x > 0 and mouse_x <= 100:
                        flag_x = 0
                    elif  mouse_x <= 200:
                        flag_x = 1
                    elif  mouse_x <= 300:
                        flag_x = 2
                    elif  mouse_x <= 400:
                        flag_x = 3
                    elif  mouse_x <= 500:
                        flag_x = 4
                    elif  mouse_x <= 600:
                        flag_x = 5
                    elif  mouse_x <= 700:
                        flag_x = 6
                    elif  mouse_x <= 800:
                        flag_x = 7
                    elif  mouse_x <= 900:
                        flag_x = 8
                    elif  mouse_x <= 1000:
                        flag_x = 9
                    if mouse_y > 0 and mouse_y <= 100:
                        flag_y = 0
                    elif  mouse_y <= 200:
                        flag_y = 1
                    elif  mouse_y <= 300:
                        flag_y = 2
                    elif  mouse_y <= 400:
                        flag_y = 3
                    elif  mouse_y <= 500:
                        flag_y = 4
                    elif  mouse_y <= 600:
                        flag_y = 5
                    elif  mouse_y <= 700:
                        flag_y = 6
                    elif  mouse_y <= 800:
                        flag_y = 7
                    elif  mouse_y <= 900:
                        flag_y = 8
                    elif  mouse_y <= 1000:
                        flag_y = 9
                    mouse_x = None
                    mouse_y = None
                if flag_x != None and flag_y != None:
                    if hairetu[flag_x+1][flag_y+1] <= 10:
                        hairetu[flag_x+1][flag_y+1] += 20
                    elif hairetu[flag_x+1][flag_y+1] >=20 and hairetu[flag_x+1][flag_y+1] <= 30:
                        hairetu[flag_x+1][flag_y+1] -= 20
                    flag_x = None
                    flag_y = None

            else:
                if mouse_x != None and mouse_y != None:
                    if mouse_x > 0 and mouse_x <= 100:
                        atack_x = 0
                    elif  mouse_x <= 200:
                        atack_x = 1
                    elif  mouse_x <= 300:
                        atack_x = 2
                    elif  mouse_x <= 400:
                        atack_x = 3
                    elif  mouse_x <= 500:
                        atack_x = 4
                    elif  mouse_x <= 600:
                        atack_x = 5
                    elif  mouse_x <= 700:
                        atack_x = 6
                    elif  mouse_x <= 800:
                        atack_x = 7
                    elif  mouse_x <= 900:
                        atack_x = 8
                    elif  mouse_x <= 1000:
                        atack_x = 9
                    if mouse_y > 0 and mouse_y <= 100:
                        atack_y = 0
                    elif  mouse_y <= 200:
                        atack_y = 1
                    elif  mouse_y <= 300:
                        atack_y = 2
                    elif  mouse_y <= 400:
                        atack_y = 3
                    elif  mouse_y <= 500:
                        atack_y = 4
                    elif  mouse_y <= 600:
                        atack_y = 5
                    elif  mouse_y <= 700:
                        atack_y = 6
                    elif  mouse_y <= 800:
                        atack_y = 7
                    elif  mouse_y <= 900:
                        atack_y = 8
                    elif  mouse_y <= 1000:
                        atack_y = 9
                    mouse_x = None
                    mouse_y = None
                if atack_x != None and atack_y != None:
                    hantei = atack(atack_x+1,atack_y+1,hairetu)
                    if hantei == False:
                        clear_check =False
                        break
                    else:
                        atack_x = None
                        atack_y = None
            for i in range(1,11):
                for j in range(1,11):
                    if hairetu[i][j] == 100:
                        pygame.draw.rect(screen,(250,250,250),Rect(100 * (i-1), 100 * (j-1) ,100,100))
                    elif hairetu[i][j] > 10 and hairetu[i][j] < 20:
                        pygame.draw.rect(screen,(250,250,250),Rect(100 * (i-1), 100 * (j-1) ,100,100))
                        screen.blit(font.render(str(hairetu[i][j]-10),False,(0,0,0)),(35 + 100 * (i-1), 25 + 100 * (j-1)))
                    else:
                        pygame.draw.rect(screen,(100,100,100),Rect(100 * (i-1), 100 * (j-1) ,100,100))
                        if hairetu[i][j] >= 20 and hairetu[i][j] <=30 :
                            screen.blit(font.render("F",False,(0,250,0)),(35 + 100 * (i-1), 25 + 100 * (j-1)))




                    pygame.draw.rect(screen,(0,0,0),Rect(100 * (i-1), 100 * (j-1),100,100),2)
            check = 0
            for i in range (1,11):
                for j in range(1,11):
                    if hairetu[i][j] < 10:
                        check += 1
            if check ==0:
                clear_check = True
                break

            pygame.display.update()
        if clear_check:
            while True:     
                clock.tick(40)
                screen.fill((250,250,250))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                for i in range(1,11):
                    for j in range(1,11):
                        if hairetu[i][j] == 100 or hairetu[i][j] ==0:
                            pygame.draw.rect(screen,(250,250,250),Rect(100 * (i-1), 100 * (j-1) ,100,100))
                        elif hairetu[i][j] > 10 and hairetu[i][j] < 20:
                            pygame.draw.rect(screen,(250,250,250),Rect(100 * (i-1), 100 * (j-1) ,100,100))
                            screen.blit(font.render(str(hairetu[i][j]-10),False,(0,0,0)),(35 + 100 * (i-1), 25 + 100 * (j-1)))
                        elif hairetu[i][j] == 10:
                            pygame.draw.rect(screen,(100,100,100),Rect(100 * (i-1), 100 * (j-1) ,100,100))
                        elif hairetu[i][j] >=20 and hairetu[i][j] <= 30:
                            pygame.draw.rect(screen,(100,100,100),Rect(100 * (i-1), 100 * (j-1) ,100,100))
                            screen.blit(font.render("F",False,(0,250,0)),(35 + 100 * (i-1), 25 + 100 * (j-1)))

                        else:
                            pygame.draw.rect(screen,(250,250,250),Rect(100 * (i-1), 100 * (j-1) ,100,100))
                            screen.blit(font.render(str(hairetu[i][j]),False,(0,0,0)),(35 + 100 * (i-1), 25 + 100 * (j-1)))
                        pygame.draw.rect(screen,(0,0,0),Rect(100 * (i-1), 100 * (j-1),100,100),2)
                screen.blit(font2.render("clear!",False,(0,0,250)),(200,300))
                pygame.display.update()

        else:
            while True:     
                clock.tick(40)
                screen.fill((250,250,250))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_n:
                            pygame.quit()
                            sys.exit()
                        if event.key == K_y:
                            restart = True
                for i in range(1,11):
                    for j in range(1,11):
                        if hairetu[i][j] == 100 or hairetu[i][j] ==0:
                            pygame.draw.rect(screen,(250,250,250),Rect(100 * (i-1), 100 * (j-1) ,100,100))
                        elif hairetu[i][j] > 10 and hairetu[i][j] < 20:
                            pygame.draw.rect(screen,(250,250,250),Rect(100 * (i-1), 100 * (j-1) ,100,100))
                            screen.blit(font.render(str(hairetu[i][j]-10),False,(0,0,0)),(35 + 100 * (i-1), 25 + 100 * (j-1)))
                        elif hairetu[i][j] == 10:
                            if i == atack_x+1 and j == atack_y+1:
                                pygame.draw.circle(screen,(0,250,0),(50 + 100 * (i-1), 50 + 100 * (j-1)),40)
                            else:
                                pygame.draw.circle(screen,(250,0,0),(50 + 100 * (i-1), 50 + 100 * (j-1)),40)
                        elif hairetu[i][j] == 30:
                            pygame.draw.rect(screen,(100,100,100),Rect(100 * (i-1), 100 * (j-1) ,100,100))
                            screen.blit(font.render("F",False,(0,250,0)),(35 + 100 * (i-1), 25 + 100 * (j-1)))
                        elif hairetu[i][j] >= 20 and hairetu[i][j] < 30:
                            pygame.draw.rect(screen,(0,250,0),Rect(100 * (i-1), 100 * (j-1) ,100,100))
                            screen.blit(font.render(str(hairetu[i][j]-20),False,(250,0,0)),(35 + 100 * (i-1), 25 + 100 * (j-1)))

                        else:
                            pygame.draw.rect(screen,(250,250,250),Rect(100 * (i-1), 100 * (j-1) ,100,100))
                            screen.blit(font.render(str(hairetu[i][j]),False,(0,0,0)),(35 + 100 * (i-1), 25 + 100 * (j-1)))
                        pygame.draw.rect(screen,(0,0,0),Rect(100 * (i-1), 100 * (j-1),100,100),2)
                screen.blit(font3.render("continue?",False,(0,0,250)),(150,400))
                screen.blit(font3.render("y or n",False,(0,0,250)),(300,550))
                pygame.display.update()
                if restart:
                    hairetu = [[0 for i in range(12)] for j in range(12)]
                    for i in range(12):
                        hairetu[i][0] = -1
                        hairetu[i][11] = -1
                        hairetu[0][i] = -1
                        hairetu[11][i] = -1
                    start_x = None
                    start_y = None
                    atack_x = None
                    atack_y = None
                    hantei = None
                    mouse_x = None
                    mouse_y = None
                    clear_chek = None
                    restart = None
                    flag = None
                    flag_x = None
                    flag_y = None
                    break

def bakudanhaichi(k,l,hairetu):
    for i in range (15):
        while True:
            x = random.randint(0,9)
            y = random.randint(0,9)
            if (x != k or y!= l) and hairetu[x][y] == 0:
                hairetu[x][y] = 10
                break
    for i in range(1,11):
        for j in range(1,11):
            if hairetu[i][j] != 10:
                tonari = 0
                if hairetu[i+1][j] == 10:
                    tonari += 1
                if hairetu[i+1][j+1] == 10:
                    tonari += 1
                if hairetu[i+1][j-1] == 10:
                    tonari += 1
                if hairetu[i][j+1] == 10:
                    tonari += 1
                if hairetu[i][j-1] == 10:
                    tonari += 1
                if hairetu[i-1][j] == 10:
                    tonari += 1
                if hairetu[i-1][j+1] == 10:
                    tonari += 1
                if hairetu[i-1][j-1] == 10:
                    tonari += 1
                hairetu[i][j] = tonari

def atack(x,y,hairetu):
    if hairetu[x][y] == 10:
        return False
    elif hairetu[x][y] == 0:
        denpan(x,y,hairetu)
        return True
    elif hairetu[x][y] > 10 and hairetu[x][y] < 20 :
        return True
    elif hairetu[x][y] < 10:
        hairetu[x][y] += 10
        return True
    else:
        return True

def denpan(x,y,hairetu):
    if hairetu[x][y] == 0:
        hairetu[x][y] = 100
        denpan(x+1,y,hairetu)
        denpan(x+1,y+1,hairetu)
        denpan(x+1,y-1,hairetu)
        denpan(x,y+1,hairetu)
        denpan(x,y-1,hairetu)
        denpan(x-1,y+1,hairetu)
        denpan(x-1,y-1,hairetu)
        denpan(x-1,y,hairetu)
    elif hairetu[x][y] > 0 and hairetu[x][y] < 10:
        hairetu[x][y] += 10



if __name__ == "__main__":
    main()
