import pygame
from pygame.locals import *
import copy

def allhyouji(field1,field2,puyo_1,puyo_2,screen,font):
  screen.fill((250,250,250))
  pygame.draw.rect(screen,(0,0,0),Rect(10,50,300,600),5)
  pygame.draw.rect(screen,(0,0,0),Rect(330,50,70,230),5)
  pygame.draw.rect(screen,(0,0,0),Rect(550,50,300,600),5)
  pygame.draw.rect(screen,(0,0,0),Rect(460,50,70,230),5)
  tokuten=font.render(str(field1.counttotal2),False,(0,0,0))
  screen.blit(tokuten,(155,660))
  tokuten_2=font.render(str(field2.counttotal2),False,(0,0,0))
  screen.blit(tokuten_2,(695,660))
  counttotal_t=field1.counttotal+field1.counttotal_a
  counttotal_t_2=field2.counttotal+field2.counttotal_a
  if field1.rensa_c!=0:
    chain=str(field1.rensa_c)+"chain"
    rensahyouji=font.render(chain,False,(250,0,0))
    screen.blit(rensahyouji,(5,660))
  if field2.rensa_c!=0:
    chain=str(field2.rensa_c)+"chain"
    rensahyouji=font.render(chain,False,(250,0,0))
    screen.blit(rensahyouji,(545,660))
  if field1.zenkeshihyouji==1:
    pygame.font.init()
    font_zen=pygame.font.Font(None,60)
    zen=font_zen.render("All Clear",False,(0,0,0))
    screen.blit(zen,(80,150))
  if field2.zenkeshihyouji==1:
    pygame.font.init()
    font_zen=pygame.font.Font(None,60)
    zen=font_zen.render("All Clear",False,(0,0,0))
    screen.blit(zen,(620,150))
  s_haichi=copy.deepcopy(field1.haichi)
  s_haichi_2=copy.deepcopy(field2.haichi)
  if field1.haichi_c==1:
    s_haichi[puyo_1.puyo1y][puyo_1.puyo1x]=puyo_1.puyo1iro
    s_haichi[puyo_1.puyo2y][puyo_1.puyo2x]=puyo_1.puyo2iro
  if field2.haichi_c==1:
    s_haichi_2[puyo_2.puyo1y][puyo_2.puyo1x]=puyo_2.puyo1iro
    s_haichi_2[puyo_2.puyo2y][puyo_2.puyo2x]=puyo_2.puyo2iro
  hyouji(s_haichi,screen)
  hyouji_2(s_haichi_2,screen)
  hyouji2(puyo_1.nexnex,screen)
  hyouji2_2(puyo_2.nexnex,screen)
  ojamahyouji(counttotal_t,field1.ojama,screen)
  ojamahyouji_2(counttotal_t_2,field2.ojama,screen)
  pygame.display.update()

def hyouji(x,screen):
  for i in range(1,14):
    for j in range(1,7):
      if x[i][j]==1:
        s=50*(12.5-i)
        s=int(s)
        k=j-0.5
        k=int(50*k)
        pygame.draw.circle(screen,(250,0,0),(k+10,s+50),25)
      elif x[i][j]==2:
        s=50*(12.5-i)
        s=int(s)
        k=j-0.5
        k=int(50*k)
        pygame.draw.circle(screen,(0,250,0),(k+10,s+50),25)
      elif x[i][j]==3:
        s=50*(12.5-i)
        s=int(s)
        k=j-0.5
        k=int(50*k)
        pygame.draw.circle(screen,(0,0,250),(k+10,s+50),25)
      elif x[i][j]==4:
        s=50*(12.5-i)
        s=int(s)
        k=j-0.5
        k=int(50*k)
        pygame.draw.circle(screen,(250,250,0),(k+10,s+50),25)
      elif x[i][j]==5:
        s=50*(12.5-i)
        s=int(s)
        k=j-0.5
        k=int(50*k)
        pygame.draw.circle(screen,(0,0,0),(k+10,s+50),25,3)
def hyouji_2(x,screen):
  for i in range(1,14):
    for j in range(1,7):
      if x[i][j]==1:
        s=50*(12.5-i)
        s=int(s)
        k=j-0.5
        k=int(50*k)
        pygame.draw.circle(screen,(250,0,0),(k+550,s+50),25)
      elif x[i][j]==2:
        s=50*(12.5-i)
        s=int(s)
        k=j-0.5
        k=int(50*k)
        pygame.draw.circle(screen,(0,250,0),(k+550,s+50),25)
      elif x[i][j]==3:
        s=50*(12.5-i)
        s=int(s)
        k=j-0.5
        k=int(50*k)
        pygame.draw.circle(screen,(0,0,250),(k+550,s+50),25)
      elif x[i][j]==4:
        s=50*(12.5-i)
        s=int(s)
        k=j-0.5
        k=int(50*k)
        pygame.draw.circle(screen,(250,250,0),(k+550,s+50),25)
      elif x[i][j]==5:
        s=50*(12.5-i)
        s=int(s)
        k=j-0.5
        k=int(50*k)
        pygame.draw.circle(screen,(0,0,0),(k+550,s+50),25,3)

def hyouji2(y,screen):
  if y[0]==1:
    pygame.draw.circle(screen,(250,0,0),(360,75),25)
  elif y[0]==2:
    pygame.draw.circle(screen,(0,250,0),(360,75),25)
  elif y[0]==3:
    pygame.draw.circle(screen,(0,0,250),(360,75),25)
  elif y[0]==4:
    pygame.draw.circle(screen,(250,250,0),(360,75),25)
  if y[1]==1:
    pygame.draw.circle(screen,(250,0,0),(360,125),25)
  elif y[1]==2:
    pygame.draw.circle(screen,(0,250,0),(360,125),25)
  elif y[1]==3:
    pygame.draw.circle(screen,(0,0,250),(360,125),25)
  elif y[1]==4:
    pygame.draw.circle(screen,(250,250,0),(360,125),25)
  if y[2]==1:
    pygame.draw.circle(screen,(250,0,0),(360,185),25)
  elif y[2]==2:
    pygame.draw.circle(screen,(0,250,0),(360,185),25)
  elif y[2]==3:
    pygame.draw.circle(screen,(0,0,250),(360,185),25)
  elif y[2]==4:
    pygame.draw.circle(screen,(250,250,0),(360,185),25)
  if y[3]==1:
    pygame.draw.circle(screen,(250,0,0),(360,235),25)
  elif y[3]==2:
    pygame.draw.circle(screen,(0,250,0),(360,235),25)
  elif y[3]==3:
    pygame.draw.circle(screen,(0,0,250),(360,235),25)
  elif y[3]==4:
    pygame.draw.circle(screen,(250,250,0),(360,235),25)
def hyouji2_2(y,screen):
  if y[0]==1:
    pygame.draw.circle(screen,(250,0,0),(500,75),25)
  elif y[0]==2:
    pygame.draw.circle(screen,(0,250,0),(500,75),25)
  elif y[0]==3:
    pygame.draw.circle(screen,(0,0,250),(500,75),25)
  elif y[0]==4:
    pygame.draw.circle(screen,(250,250,0),(500,75),25)
  if y[1]==1:
    pygame.draw.circle(screen,(250,0,0),(500,125),25)
  elif y[1]==2:
    pygame.draw.circle(screen,(0,250,0),(500,125),25)
  elif y[1]==3:
    pygame.draw.circle(screen,(0,0,250),(500,125),25)
  elif y[1]==4:
    pygame.draw.circle(screen,(250,250,0),(500,125),25)
  if y[2]==1:
    pygame.draw.circle(screen,(250,0,0),(500,185),25)
  elif y[2]==2:
    pygame.draw.circle(screen,(0,250,0),(500,185),25)
  elif y[2]==3:
    pygame.draw.circle(screen,(0,0,250),(500,185),25)
  elif y[2]==4:
    pygame.draw.circle(screen,(250,250,0),(500,185),25)
  if y[3]==1:
    pygame.draw.circle(screen,(250,0,0),(500,235),25)
  elif y[3]==2:
    pygame.draw.circle(screen,(0,250,0),(500,235),25)
  elif y[3]==3:
    pygame.draw.circle(screen,(0,0,250),(500,235),25)
  elif y[3]==4:
    pygame.draw.circle(screen,(250,250,0),(500,235),25)

def hyouji3(x,screen):
  for i in range(6):
    if x[i]==1:
     pygame.draw.circle(screen,(0,0,0),(35+50*i,35),15,2)
    elif x[i]==2:
      pygame.draw.circle(screen,(0,0,0),(35+50*i,25),25,2)
    elif x[i]==3:
      pygame.draw.circle(screen,(250,0,0),(35+50*i,25),25)
    elif x[i]==4:
      pygame.draw.circle(screen,(250,250,0),(35+50*i,25),25)
def hyouji3_2(x,screen):
  for i in range(6):
    if x[i]==1:
      pygame.draw.circle(screen,(0,0,0),(575+50*i,35),15,2)
    elif x[i]==2:
      pygame.draw.circle(screen,(0,0,0),(575+50*i,25),25,2)
    elif x[i]==3:
      pygame.draw.circle(screen,(250,0,0),(575+50*i,25),25)
    elif x[i]==4:
      pygame.draw.circle(screen,(250,250,0),(575+50*i,25),25)

def ojamahyouji(x,y,screen):
    y[0]=0
    y[1]=0
    y[2]=0
    y[3]=0
    y[4]=0
    y[5]=0
    x=x//70
    hoshi=x//180
    iwa=(x % 180)//30
    oo=(x % 30)//6
    syou=x % 6
    go1=hoshi+iwa
    go2=hoshi+iwa+oo
    go3=hoshi+iwa+oo+syou
    if go1>6:
      go1=6
    if go2>6:
      go2=6
    if go3>6:
      go3=6
    for i in range(hoshi):
      y[i]=4
    for i in range(hoshi,go1):
      y[i]=3
    for i in range(go1,go2):
      y[i]=2
    for i in range(go2,go3):
      y[i]=1
    hyouji3_2(y,screen)
def ojamahyouji_2(x,y,screen):
    y[0]=0
    y[1]=0
    y[2]=0
    y[3]=0
    y[4]=0
    y[5]=0
    x=x//70
    hoshi=x//180
    iwa=(x % 180)//30
    oo=(x % 30)//6
    syou=x % 6
    go1=hoshi+iwa
    go2=hoshi+iwa+oo
    go3=hoshi+iwa+oo+syou
    if go1>6:
      go1=6
    if go2>6:
      go2=6
    if go3>6:
      go3=6
    for i in range(hoshi):
      y[i]=4
    for i in range(hoshi,go1):
      y[i]=3
    for i in range(go1,go2):
      y[i]=2
    for i in range(go2,go3):
      y[i]=1
    hyouji3(y,screen)

