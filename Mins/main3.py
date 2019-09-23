import pygame
from pygame.locals import *
import random
import sys

def main():
    pygame.init()
    pygame.display.set_caption("Minesweeper")
    clock = pygame.time.Clock()
    field = Field()
    # game start
    while True :
        timecount = 0
        # syote
        while True:     
            clock.tick(40)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        field.mouse_x,field.mouse_y = event.pos
            if field.mouse_x != None and field.mouse_y != None:
                field.start()
            if field.start_x != None and field.start_y != None:
                field.bakudanhaichi()
                break
            field.hyouji0()   
        # play gamen
        while True:     
            clock.tick(40)
            timecount += 1
            if timecount >= 40 :
                field.time += 1
                timecount = 0
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_f:
                        if field.flag == 0:
                            field.flag = 1
                        elif field.flag == 1:
                            field.flag = 2
                        else:
                            field.flag = 0
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    field.mouse_x,field.mouse_y = event.pos
            if field.flag != 0 :
                if field.mouse_x != None and field.mouse_y != None:
                    field.flagichi()
                if field.flag_x != None and field.flag_y != None:
                    field.flagkirikae()
            else:
                if field.mouse_x != None and field.mouse_y != None:
                    field.atackichi()
                if field.atack_x != None and field.atack_y != None:
                    hantei = field.atack()
                    if hantei == False:
                        field.clear_check = False
                        break
                    else:
                        field.atack_x = None
                        field.atack_y = None
            check = 0
            for i in range (1,11):
                for j in range(1,11):
                    if field.hairetu[i][j].bakudan == False and field.hairetu[i][j].open == False:
                        check += 1
            if check ==0:
                field.clear_check = True
                break
            field.hyouji1()
        if field.clear_check:
            # clear
            while True:     
                clock.tick(40)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_n:
                            pygame.quit()
                            sys.exit()
                        if event.key == K_y:
                            field.restart = True
                if field.restart:
                    field = Field()
                    break
                field.hyouji1()
        else:
            # out   
            while True:     
                clock.tick(40)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_n:
                            pygame.quit()
                            sys.exit()
                        if event.key == K_y:
                            field.restart = True
                if field.restart:
                    field = Field()
                    break
                field.hyouji2()





class Field():
    def __init__(self):
        self.screen=pygame.display.set_mode((1000,1100))
        self.hairetu = [[Cell() for i in range(12)] for j in range(12)]
        for i in range(12):
            self.hairetu[i][0].wall = True
            self.hairetu[i][11].wall = True
            self.hairetu[0][i].wall = True
            self.hairetu[11][i].wall = True
        self.start_x = None
        self.start_y = None
        self.atack_x = None
        self.atack_y = None
        self.hantei = None
        self.mouse_x = None
        self.mouse_y = None
        self.clear_check = None
        self.restart = None
        self.flag = 0
        self.flag_x = None
        self.flag_y = None
        self.font = pygame.font.Font(None,80)
        self.font2 = pygame.font.Font(None,300)
        self.font3 = pygame.font.Font(None,200)
        self.time = 0

    def start(self):
       if self.mouse_x > 0 and self.mouse_x <= 100:
           self.start_x = 0
       elif  self.mouse_x <= 200:
           self.start_x = 1
       elif  self.mouse_x <= 300:
           self.start_x = 2
       elif  self.mouse_x <= 400:
           self.start_x = 3
       elif  self.mouse_x <= 500:
           self.start_x = 4
       elif  self.mouse_x <= 600:
           self.start_x = 5
       elif  self.mouse_x <= 700:
           self.start_x = 6
       elif  self.mouse_x <= 800:
           self.start_x = 7
       elif  self.mouse_x <= 900:
           self.start_x = 8
       elif  self.mouse_x <= 1000:
           self.start_x = 9
       if self.mouse_y > 100 and self.mouse_y <= 200:
           self.start_y = 0
       elif  self.mouse_y <= 300:
           self.start_y = 1
       elif  self.mouse_y <= 400:
           self.start_y = 2
       elif  self.mouse_y <= 500:
           self.start_y = 3
       elif  self.mouse_y <= 600:
           self.start_y = 4
       elif  self.mouse_y <= 700:
           self.start_y = 5
       elif  self.mouse_y <= 800:
           self.start_y = 6
       elif  self.mouse_y <= 900:
           self.start_y = 7
       elif  self.mouse_y <= 1000:
           self.start_y = 8
       elif  self.mouse_y <= 1100:
           self.start_y = 9
       self.mouse_x = None
       self.mouse_y = None

    def bakudanhaichi(self):
        for i in range (15):
            while True:
                x = random.randint(1,10)
                y = random.randint(1,10)
                if (x != self.start_x+ 1 or y != self.start_y + 1) and self.hairetu[x][y].bakudan == False:
                    self.hairetu[x][y].bakudan = True
                    break
        for i in range(1,11):
            for j in range(1,11):
                if self.hairetu[i][j].bakudan == False:
                    tonari = 0
                    if self.hairetu[i+1][j].bakudan:
                        tonari += 1
                    if self.hairetu[i+1][j+1].bakudan:
                        tonari += 1
                    if self.hairetu[i+1][j-1].bakudan:
                        tonari += 1
                    if self.hairetu[i][j+1].bakudan:
                        tonari += 1
                    if self.hairetu[i][j-1].bakudan:
                        tonari += 1
                    if self.hairetu[i-1][j].bakudan:
                        tonari += 1
                    if self.hairetu[i-1][j+1].bakudan:
                        tonari += 1
                    if self.hairetu[i-1][j-1].bakudan:
                        tonari += 1
                    self.hairetu[i][j].bakudanrinsetu = tonari
        self.atack_x = self.start_x
        self.atack_y = self.start_y

    def flagichi(self):
        if self.mouse_x > 0 and self.mouse_x <= 100:
            self.flag_x = 0
        elif  self.mouse_x <= 200:
            self.flag_x = 1
        elif  self.mouse_x <= 300:
            self.flag_x = 2
        elif  self.mouse_x <= 400:
            self.flag_x = 3
        elif  self.mouse_x <= 500:
            self.flag_x = 4
        elif  self.mouse_x <= 600:
            self.flag_x = 5
        elif  self.mouse_x <= 700:
            self.flag_x = 6
        elif  self.mouse_x <= 800:
            self.flag_x = 7
        elif  self.mouse_x <= 900:
            self.flag_x = 8
        elif  self.mouse_x <= 1000:
            self.flag_x = 9
        if self.mouse_y > 100 and self.mouse_y <= 200:
            self.flag_y = 0
        elif  self.mouse_y <= 300:
            self.flag_y = 1
        elif  self.mouse_y <= 400:
            self.flag_y = 2
        elif  self.mouse_y <= 500:
            self.flag_y = 3
        elif  self.mouse_y <= 600:
            self.flag_y = 4
        elif  self.mouse_y <= 700:
            self.flag_y = 5
        elif  self.mouse_y <= 800:
            self.flag_y = 6
        elif  self.mouse_y <= 900:
            self.flag_y = 7
        elif  self.mouse_y <= 1000:
            self.flag_y = 8
        elif  self.mouse_y <= 1100:
            self.flag_y = 9
        self.mouse_x = None
        self.mouse_y = None

    def flagkirikae(self):
        if self.hairetu[self.flag_x+1][self.flag_y+1].flag == 0:
            if self.flag == 1:
                self.hairetu[self.flag_x+1][self.flag_y+1].flag = 1
            elif self.flag == 2:
                self.hairetu[self.flag_x+1][self.flag_y+1].flag = 2
        elif self.hairetu[self.flag_x+1][self.flag_y+1].flag == 1:
            self.hairetu[self.flag_x+1][self.flag_y+1].flag = 0
        elif self.hairetu[self.flag_x+1][self.flag_y+1].flag == 2:
            self.hairetu[self.flag_x+1][self.flag_y+1].flag = 0
        self.flag_x = None
        self.flag_y = None

    def atackichi(self):
        if self.mouse_x > 0 and self.mouse_x <= 100:
            self.atack_x = 0
        elif  self.mouse_x <= 200:
            self.atack_x = 1
        elif  self.mouse_x <= 300:
            self.atack_x = 2
        elif  self.mouse_x <= 400:
            self.atack_x = 3
        elif  self.mouse_x <= 500:
            self.atack_x = 4
        elif  self.mouse_x <= 600:
            self.atack_x = 5
        elif  self.mouse_x <= 700:
            self.atack_x = 6
        elif  self.mouse_x <= 800:
            self.atack_x = 7
        elif  self.mouse_x <= 900:
            self.atack_x = 8
        elif  self.mouse_x <= 1000:
            self.atack_x = 9
        if self.mouse_y > 100 and self.mouse_y <= 200:
            self.atack_y = 0
        elif  self.mouse_y <= 300:
            self.atack_y = 1
        elif  self.mouse_y <= 400:
            self.atack_y = 2
        elif  self.mouse_y <= 500:
            self.atack_y = 3
        elif  self.mouse_y <= 600:
            self.atack_y = 4
        elif  self.mouse_y <= 700:
            self.atack_y = 5
        elif  self.mouse_y <= 800:
            self.atack_y = 6
        elif  self.mouse_y <= 900:
            self.atack_y = 7
        elif  self.mouse_y <= 1000:
            self.atack_y = 8
        elif  self.mouse_y <= 1100:
            self.atack_y = 9
        self.mouse_x = None
        self.mouse_y = None

    def atack(self):
        x = self.atack_x + 1
        y = self.atack_y + 1
        if self.hairetu[x][y].flag != 0:
            return True
        if self.hairetu[x][y].open == False:
            if self.hairetu[x][y].bakudan:
                return False
            elif self.hairetu[x][y].bakudanrinsetu == 0:
                self.denpan(x,y)
                return True
            else:
                self.hairetu[x][y].open = True
                return True
        else:
            return True

    def denpan(self,x,y):
        if self.hairetu[x][y].wall:
            return 0
        if self.hairetu[x][y].flag != 0:
            return 0
        if self.hairetu[x][y].open == False:
            if self.hairetu[x][y].bakudanrinsetu == 0: 
                self.hairetu[x][y].open = True
                self.denpan(x+1,y)
                self.denpan(x+1,y+1)
                self.denpan(x+1,y-1)
                self.denpan(x,y+1)
                self.denpan(x,y-1)
                self.denpan(x-1,y+1)
                self.denpan(x-1,y-1)
                self.denpan(x-1,y)
            else:
                self.hairetu[x][y].open = True

    def hyouji0(self):
        self.screen.fill((250,250,250))
        for i in range(1,11):
            for j in range(1,11):
                pygame.draw.rect(self.screen,(100,100,100),Rect(100 * (i-1), 100 + 100 * (j-1),100,100))
                pygame.draw.rect(self.screen,(0,0,0),Rect(100 * (i-1), 100 + 100 * (j-1),100,100),2)
        self.uegamenhyouji()
        pygame.display.update()
  

    def hyouji1(self):
        self.screen.fill((250,250,250))
        for i in range(1,11):
            for j in range(1,11):
                if self.hairetu[i][j].open:
                    if self.hairetu[i][j].bakudanrinsetu != 0:
                        self.screen.blit(self.font.render(str(self.hairetu[i][j].bakudanrinsetu),False,(0,0,0)),(35 + 100 * (i-1), 125 + 100 * (j-1)))
                else:
                    pygame.draw.rect(self.screen,(100,100,100),Rect(100 * (i-1),100 + 100 * (j-1) ,100,100))
                    if self.hairetu[i][j].flag == 1:
                        self.screen.blit(self.font.render("F",False,(0,250,0)),(35 + 100 * (i-1), 125 + 100 * (j-1)))
                    elif self.hairetu[i][j].flag == 2:
                        self.screen.blit(self.font.render("F",False,(0,0,250)),(35 + 100 * (i-1), 125 + 100 * (j-1)))
                pygame.draw.rect(self.screen,(0,0,0),Rect(100 * (i-1),100 + 100 * (j-1),100,100),2)
        self.uegamenhyouji()
        if self.clear_check:
            self.screen.blit(self.font2.render("clear!",False,(0,0,250)),(200,400))
        pygame.display.update()


    def hyouji2(self):
        self.screen.fill((250,250,250))
        for i in range(1,11):
            for j in range(1,11):
                if self.hairetu[i][j].bakudan:
                    if self.hairetu[i][j].flag == 0:
                        if i == self.atack_x+1 and j == self.atack_y+1:
                            pygame.draw.circle(self.screen,(0,250,0),(50 + 100 * (i-1), 150 + 100 * (j-1)),40)
                        else:
                            pygame.draw.circle(self.screen,(250,0,0),(50 + 100 * (i-1), 150 + 100 * (j-1)),40)
                    elif self.hairetu[i][j].flag == 1:
                        pygame.draw.rect(self.screen,(100,100,100),Rect(100 * (i-1),100 + 100 * (j-1) ,100,100))
                        self.screen.blit(self.font.render("F",False,(0,250,0)),(35 + 100 * (i-1), 125 + 100 * (j-1)))
                    elif self.hairetu[i][j].flag == 2:
                        pygame.draw.rect(self.screen,(100,100,100),Rect(100 * (i-1),100 + 100 * (j-1) ,100,100))
                        self.screen.blit(self.font.render("F",False,(0,0,250)),(35 + 100 * (i-1), 125 + 100 * (j-1)))
                elif self.hairetu[i][j].flag == 1:
                    pygame.draw.rect(self.screen,(0,250,0),Rect(100 * (i-1),100 + 100 * (j-1) ,100,100))
                    self.screen.blit(self.font.render(str(self.hairetu[i][j].bakudanrinsetu),False,(250,0,0)),(35 + 100 * (i-1), 125 + 100 * (j-1)))
                elif self.hairetu[i][j].flag == 2:
                    pygame.draw.rect(self.screen,(0,0,250),Rect(100 * (i-1),100 + 100 * (j-1) ,100,100))
                    self.screen.blit(self.font.render(str(self.hairetu[i][j].bakudanrinsetu),False,(250,0,0)),(35 + 100 * (i-1), 125 + 100 * (j-1)))
                elif self.hairetu[i][j].bakudanrinsetu != 0: 
                    self.screen.blit(self.font.render(str(self.hairetu[i][j].bakudanrinsetu),False,(0,0,0)),(35 + 100 * (i-1), 125 + 100 * (j-1)))
                pygame.draw.rect(self.screen,(0,0,0),Rect(100 * (i-1),100 + 100 * (j-1),100,100),2)
        self.screen.blit(self.font3.render("continue?",False,(0,0,250)),(150,500))
        self.screen.blit(self.font3.render("y or n",False,(0,0,250)),(300,650))
        self.uegamenhyouji()
        pygame.display.update()


    def uegamenhyouji(self):
        pygame.draw.rect(self.screen,(200,200,250),Rect(0,0,1000,100))
#        pygame.draw.rect(self.screen,(0,0,250),Rect(0,1000,1000,95),10)
        count = 0
        count2 = 0
        for i in range(1,11):
            for j in range(1,11):
                if self.hairetu[i][j].flag == 1:
                    count += 1
                elif self.hairetu[i][j].flag == 2:
                    count2 += 1
        if self.flag == 1:
            self.screen.blit(self.font.render("F : " + str(count),False,(0,200,0)),(230,25))
        elif self.flag == 2:
            self.screen.blit(self.font.render("F : " + str(count2),False,(0,0,200)),(230,25))
        else:
            self.screen.blit(self.font.render("F : " + str(count + count2),False,(250,0,0)),(230,25))
        self.screen.blit(self.font.render("time : " + str(self.time) +"s",False,(250,0,250)),(530,25) )

class Cell():
    def __init__ (self):
        self.bakudan = False
        self.bakudanrinsetu = None
        self.flag = 0
        self.open = False
        self.wall = False



if __name__ == "__main__":
    main()
