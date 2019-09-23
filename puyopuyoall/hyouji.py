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

def allhyouji_f(field1,field2,puyo_1,puyo_2,screen,font,fever1,fever2):
  screen.fill((250,250,250))
  pygame.draw.rect(screen,(0,0,0),Rect(10,50,300,600),5)
  pygame.draw.rect(screen,(0,0,0),Rect(330,50,70,230),5)
  pygame.draw.rect(screen,(0,0,0),Rect(550,50,300,600),5)
  pygame.draw.rect(screen,(0,0,0),Rect(460,50,70,230),5)
  pygame.draw.circle(screen,(0,0,0),(380,310),16,2)
  pygame.draw.circle(screen,(0,0,0),(410,360),16,2)
  pygame.draw.circle(screen,(0,0,0),(410,410),16,2)
  pygame.draw.circle(screen,(0,0,0),(380,460),16,2)
  pygame.draw.circle(screen,(0,0,0),(365,510),16,2)
  pygame.draw.circle(screen,(0,0,0),(365,560),16,2)
  pygame.draw.circle(screen,(0,0,0),(365,610),16,2)
  pygame.draw.circle(screen,(0,0,0),(480,310),16,2)
  pygame.draw.circle(screen,(0,0,0),(450,360),16,2)
  pygame.draw.circle(screen,(0,0,0),(450,410),16,2)
  pygame.draw.circle(screen,(0,0,0),(480,460),16,2)
  pygame.draw.circle(screen,(0,0,0),(495,510),16,2)
  pygame.draw.circle(screen,(0,0,0),(495,560),16,2)
  pygame.draw.circle(screen,(0,0,0),(495,610),16,2)
  font2=pygame.font.Font(None,70)
  if fever1.fehantei:
    if fever1.fetime>=10:
      fetime=font2.render(str(fever1.fetime),False,(0,0,0))
      screen.blit(fetime,(130,60))
    else:
      fetime=font2.render("0"+str(fever1.fetime),False,(0,0,0))
      screen.blit(fetime,(130,60))
    pygame.draw.circle(screen,(250,0,0),(365,610),16)
    pygame.draw.circle(screen,(250,0,0),(365,560),16)
    pygame.draw.circle(screen,(250,0,0),(365,510),16)
    pygame.draw.circle(screen,(250,0,0),(380,460),16)
    pygame.draw.circle(screen,(250,0,0),(410,410),16)
    pygame.draw.circle(screen,(250,0,0),(410,360),16)
    pygame.draw.circle(screen,(250,0,0),(380,310),16)
  else:
    fetime=font2.render(str(fever1.fetime),False,(0,0,0))
    screen.blit(fetime,(330,365))
    if fever1.fegauge==1:
      pygame.draw.circle(screen,(250,250,0),(365,610),16)
    elif fever1.fegauge==2:
      pygame.draw.circle(screen,(250,250,0),(365,610),16)
      pygame.draw.circle(screen,(250,250,0),(365,560),16)
    elif fever1.fegauge==3:
      pygame.draw.circle(screen,(250,250,0),(365,610),16)
      pygame.draw.circle(screen,(250,250,0),(365,560),16)
      pygame.draw.circle(screen,(250,250,0),(365,510),16)
    elif fever1.fegauge==4:
      pygame.draw.circle(screen,(250,250,0),(365,610),16)
      pygame.draw.circle(screen,(250,250,0),(365,560),16)
      pygame.draw.circle(screen,(250,250,0),(365,510),16)
      pygame.draw.circle(screen,(250,250,0),(380,460),16)
    elif fever1.fegauge==5:
      pygame.draw.circle(screen,(250,250,0),(365,610),16)
      pygame.draw.circle(screen,(250,250,0),(365,560),16)
      pygame.draw.circle(screen,(250,250,0),(365,510),16)
      pygame.draw.circle(screen,(250,250,0),(380,460),16)
      pygame.draw.circle(screen,(250,250,0),(410,410),16)
    elif fever1.fegauge==6:
      pygame.draw.circle(screen,(250,250,0),(365,610),16)
      pygame.draw.circle(screen,(250,250,0),(365,560),16)
      pygame.draw.circle(screen,(250,250,0),(365,510),16)
      pygame.draw.circle(screen,(250,250,0),(380,460),16)
      pygame.draw.circle(screen,(250,250,0),(410,410),16)
      pygame.draw.circle(screen,(250,250,0),(410,360),16)
    elif fever1.fegauge==7:
      pygame.draw.circle(screen,(250,250,0),(365,610),16)
      pygame.draw.circle(screen,(250,250,0),(365,560),16)
      pygame.draw.circle(screen,(250,250,0),(365,510),16)
      pygame.draw.circle(screen,(250,250,0),(380,460),16)
      pygame.draw.circle(screen,(250,250,0),(410,410),16)
      pygame.draw.circle(screen,(250,250,0),(410,360),16)
      pygame.draw.circle(screen,(250,250,0),(380,310),16)
  if fever2.fehantei:
    if fever2.fetime>=10:
      fetime=font2.render(str(fever2.fetime),False,(0,0,0))
      screen.blit(fetime,(670,60))
    else:
      fetime=font2.render("0"+str(fever2.fetime),False,(0,0,0))
      screen.blit(fetime,(670,60))
    pygame.draw.circle(screen,(250,0,0),(495,610),16)
    pygame.draw.circle(screen,(250,0,0),(495,560),16)
    pygame.draw.circle(screen,(250,0,0),(495,510),16)
    pygame.draw.circle(screen,(250,0,0),(480,460),16)
    pygame.draw.circle(screen,(250,0,0),(450,410),16)
    pygame.draw.circle(screen,(250,0,0),(450,360),16)
    pygame.draw.circle(screen,(250,0,0),(480,310),16)
  else:
    fetime=font2.render(str(fever2.fetime),False,(0,0,0))
    screen.blit(fetime,(470,365))
    if fever2.fegauge==1:
      pygame.draw.circle(screen,(250,250,0),(495,610),16)
    elif fever2.fegauge==2:
      pygame.draw.circle(screen,(250,250,0),(495,610),16)
      pygame.draw.circle(screen,(250,250,0),(495,560),16)
    elif fever2.fegauge==3:
      pygame.draw.circle(screen,(250,250,0),(495,610),16)
      pygame.draw.circle(screen,(250,250,0),(495,560),16)
      pygame.draw.circle(screen,(250,250,0),(495,510),16)
    elif fever2.fegauge==4:
      pygame.draw.circle(screen,(250,250,0),(495,610),16)
      pygame.draw.circle(screen,(250,250,0),(495,560),16)
      pygame.draw.circle(screen,(250,250,0),(495,510),16)
      pygame.draw.circle(screen,(250,250,0),(480,460),16)
    elif fever2.fegauge==5:
      pygame.draw.circle(screen,(250,250,0),(495,610),16)
      pygame.draw.circle(screen,(250,250,0),(495,560),16)
      pygame.draw.circle(screen,(250,250,0),(495,510),16)
      pygame.draw.circle(screen,(250,250,0),(480,460),16)
      pygame.draw.circle(screen,(250,250,0),(450,410),16)
    elif fever2.fegauge==6:
      pygame.draw.circle(screen,(250,250,0),(495,610),16)
      pygame.draw.circle(screen,(250,250,0),(495,560),16)
      pygame.draw.circle(screen,(250,250,0),(495,510),16)
      pygame.draw.circle(screen,(250,250,0),(480,460),16)
      pygame.draw.circle(screen,(250,250,0),(450,410),16)
      pygame.draw.circle(screen,(250,250,0),(450,360),16)
    elif fever2.fegauge==7:
      pygame.draw.circle(screen,(250,250,0),(495,610),16)
      pygame.draw.circle(screen,(250,250,0),(495,560),16)
      pygame.draw.circle(screen,(250,250,0),(495,510),16)
      pygame.draw.circle(screen,(250,250,0),(480,460),16)
      pygame.draw.circle(screen,(250,250,0),(450,410),16)
      pygame.draw.circle(screen,(250,250,0),(450,360),16)
      pygame.draw.circle(screen,(250,250,0),(480,310),16)
   
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
    if puyo_1.puyosuu_c==2:
      s_haichi[puyo_1.puyo1y][puyo_1.puyo1x]=puyo_1.puyo1iro
      s_haichi[puyo_1.puyo2y][puyo_1.puyo2x]=puyo_1.puyo2iro
    elif puyo_1.puyosuu_c==3:
      s_haichi[puyo_1.puyo1y][puyo_1.puyo1x]=puyo_1.puyo1iro
      s_haichi[puyo_1.puyo2y][puyo_1.puyo2x]=puyo_1.puyo2iro
      s_haichi[puyo_1.puyo3y][puyo_1.puyo3x]=puyo_1.puyo3iro
    elif puyo_1.puyosuu_c==4 or puyo_1.puyosuu_c==5:
      s_haichi[puyo_1.puyo1y][puyo_1.puyo1x]=puyo_1.puyo1iro
      s_haichi[puyo_1.puyo2y][puyo_1.puyo2x]=puyo_1.puyo2iro
      s_haichi[puyo_1.puyo3y][puyo_1.puyo3x]=puyo_1.puyo3iro
      s_haichi[puyo_1.puyo4y][puyo_1.puyo4x]=puyo_1.puyo4iro
  if field2.haichi_c==1:
    if puyo_2.puyosuu_c==2:
      s_haichi_2[puyo_2.puyo1y][puyo_2.puyo1x]=puyo_2.puyo1iro
      s_haichi_2[puyo_2.puyo2y][puyo_2.puyo2x]=puyo_2.puyo2iro
    elif puyo_2.puyosuu_c==3:
      s_haichi_2[puyo_2.puyo1y][puyo_2.puyo1x]=puyo_2.puyo1iro
      s_haichi_2[puyo_2.puyo2y][puyo_2.puyo2x]=puyo_2.puyo2iro
      s_haichi_2[puyo_2.puyo3y][puyo_2.puyo3x]=puyo_2.puyo3iro
    elif puyo_2.puyosuu_c==4 or puyo_2.puyosuu_c==5:
      s_haichi_2[puyo_2.puyo1y][puyo_2.puyo1x]=puyo_2.puyo1iro
      s_haichi_2[puyo_2.puyo2y][puyo_2.puyo2x]=puyo_2.puyo2iro
      s_haichi_2[puyo_2.puyo3y][puyo_2.puyo3x]=puyo_2.puyo3iro
      s_haichi_2[puyo_2.puyo4y][puyo_2.puyo4x]=puyo_2.puyo4iro
  hyouji(s_haichi,screen)
  hyouji_2(s_haichi_2,screen)
  hyouji2_f(puyo_1.nexnex,screen)
  hyouji2_2_f(puyo_2.nexnex,screen)
  ojamahyouji_ff(field1.counttotal_f,field1.ojama_f,screen)
  ojamahyouji_ff_2(field2.counttotal_f,field2.ojama_f,screen)
  ojamahyouji_f(counttotal_t,field1.ojama,screen)
  ojamahyouji_f_2(counttotal_t_2,field2.ojama,screen)
  pygame.display.update()



def hyouji(x,screen):
  for i in range(1,13):
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
  for i in range(1,13):
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

def hyouji2_f(y,screen):
  if y[0][3]==0:
    if y[0][0]==1:
      pygame.draw.circle(screen,(250,0,0),(360,75),25)
    elif y[0][0]==2:
      pygame.draw.circle(screen,(0,250,0),(360,75),25)
    elif y[0][0]==3:
      pygame.draw.circle(screen,(0,0,250),(360,75),25)
    elif y[0][0]==4:
      pygame.draw.circle(screen,(250,250,0),(360,75),25)
    if y[0][1]==1:
      pygame.draw.circle(screen,(250,0,0),(360,125),25)
    elif y[0][1]==2:
      pygame.draw.circle(screen,(0,250,0),(360,125),25)
    elif y[0][1]==3:
      pygame.draw.circle(screen,(0,0,250),(360,125),25)
    elif y[0][1]==4:
      pygame.draw.circle(screen,(250,250,0),(360,125),25)
  else:
    if y[0][0]==1:
      pygame.draw.circle(screen,(250,0,0),(345,85),15)
    elif y[0][0]==2:
      pygame.draw.circle(screen,(0,250,0),(345,85),15)
    elif y[0][0]==3:
      pygame.draw.circle(screen,(0,0,250),(345,85),15)
    elif y[0][0]==4:
      pygame.draw.circle(screen,(250,250,0),(345,85),15)
    if y[0][1]==1:
      pygame.draw.circle(screen,(250,0,0),(345,115),15)
    elif y[0][1]==2:
      pygame.draw.circle(screen,(0,250,0),(345,115),15)
    elif y[0][1]==3:
      pygame.draw.circle(screen,(0,0,250),(345,115),15)
    elif y[0][1]==4:
      pygame.draw.circle(screen,(250,250,0),(345,115),15)
    if y[0][2]==1:
      pygame.draw.circle(screen,(250,0,0),(375,85),15)
    elif y[0][2]==2:
      pygame.draw.circle(screen,(0,250,0),(375,85),15)
    elif y[0][2]==3:
      pygame.draw.circle(screen,(0,0,250),(375,85),15)
    elif y[0][2]==4:
      pygame.draw.circle(screen,(250,250,0),(375,85),15)
    if y[0][3]==1:
      pygame.draw.circle(screen,(250,0,0),(375,115),15)
    elif y[0][3]==2:
      pygame.draw.circle(screen,(0,250,0),(375,115),15)
    elif y[0][3]==3:
      pygame.draw.circle(screen,(0,0,250),(375,115),15)
    elif y[0][3]==4:
      pygame.draw.circle(screen,(250,250,0),(375,115),15)
  if y[1][3]==0:
    if y[1][0]==1:
      pygame.draw.circle(screen,(250,0,0),(360,185),25)
    elif y[1][0]==2:
      pygame.draw.circle(screen,(0,250,0),(360,185),25)
    elif y[1][0]==3:
      pygame.draw.circle(screen,(0,0,250),(360,185),25)
    elif y[1][0]==4:
      pygame.draw.circle(screen,(250,250,0),(360,185),25)
    if y[1][1]==1:
      pygame.draw.circle(screen,(250,0,0),(360,235),25)
    elif y[1][1]==2:
      pygame.draw.circle(screen,(0,250,0),(360,235),25)
    elif y[1][1]==3:
      pygame.draw.circle(screen,(0,0,250),(360,235),25)
    elif y[1][1]==4:
      pygame.draw.circle(screen,(250,250,0),(360,235),25)
  else:
    if y[1][0]==1:
      pygame.draw.circle(screen,(250,0,0),(345,195),15)
    elif y[1][0]==2:
      pygame.draw.circle(screen,(0,250,0),(345,195),15)
    elif y[1][0]==3:
      pygame.draw.circle(screen,(0,0,250),(345,195),15)
    elif y[1][0]==4:
      pygame.draw.circle(screen,(250,250,0),(345,195),15)
    if y[1][1]==1:
      pygame.draw.circle(screen,(250,0,0),(345,225),15)
    elif y[1][1]==2:
      pygame.draw.circle(screen,(0,250,0),(345,225),15)
    elif y[1][1]==3:
      pygame.draw.circle(screen,(0,0,250),(345,225),15)
    elif y[1][1]==4:
      pygame.draw.circle(screen,(250,250,0),(345,225),15)
    if y[1][2]==1:
      pygame.draw.circle(screen,(250,0,0),(375,195),15)
    elif y[1][2]==2:
      pygame.draw.circle(screen,(0,250,0),(375,195),15)
    elif y[1][2]==3:
      pygame.draw.circle(screen,(0,0,250),(375,195),15)
    elif y[1][2]==4:
      pygame.draw.circle(screen,(250,250,0),(375,195),15)
    if y[1][3]==1:
      pygame.draw.circle(screen,(250,0,0),(375,225),15)
    elif y[1][3]==2:
      pygame.draw.circle(screen,(0,250,0),(375,225),15)
    elif y[1][3]==3:
      pygame.draw.circle(screen,(0,0,250),(375,225),15)
    elif y[1][3]==4:
      pygame.draw.circle(screen,(250,250,0),(375,225),15)
    
def hyouji2_2_f(y,screen):
  if y[0][3]==0:
    if y[0][0]==1:
      pygame.draw.circle(screen,(250,0,0),(500,75),25)
    elif y[0][0]==2:
      pygame.draw.circle(screen,(0,250,0),(500,75),25)
    elif y[0][0]==3:
      pygame.draw.circle(screen,(0,0,250),(500,75),25)
    elif y[0][0]==4:
      pygame.draw.circle(screen,(250,250,0),(500,75),25)
    if y[0][1]==1:
      pygame.draw.circle(screen,(250,0,0),(500,125),25)
    elif y[0][1]==2:
      pygame.draw.circle(screen,(0,250,0),(500,125),25)
    elif y[0][1]==3:
      pygame.draw.circle(screen,(0,0,250),(500,125),25)
    elif y[0][1]==4:
      pygame.draw.circle(screen,(250,250,0),(500,125),25)
  else:
    if y[0][0]==1:
      pygame.draw.circle(screen,(250,0,0),(485,85),15)
    elif y[0][0]==2:
      pygame.draw.circle(screen,(0,250,0),(485,85),15)
    elif y[0][0]==3:
      pygame.draw.circle(screen,(0,0,250),(485,85),15)
    elif y[0][0]==4:
      pygame.draw.circle(screen,(250,250,0),(485,85),15)
    if y[0][1]==1:
      pygame.draw.circle(screen,(250,0,0),(485,115),15)
    elif y[0][1]==2:
      pygame.draw.circle(screen,(0,250,0),(485,115),15)
    elif y[0][1]==3:
      pygame.draw.circle(screen,(0,0,250),(485,115),15)
    elif y[0][1]==4:
      pygame.draw.circle(screen,(250,250,0),(485,115),15)
    if y[0][2]==1:
      pygame.draw.circle(screen,(250,0,0),(515,85),15)
    elif y[0][2]==2:
      pygame.draw.circle(screen,(0,250,0),(515,85),15)
    elif y[0][2]==3:
      pygame.draw.circle(screen,(0,0,250),(515,85),15)
    elif y[0][2]==4:
      pygame.draw.circle(screen,(250,250,0),(515,85),15)
    if y[0][3]==1:
      pygame.draw.circle(screen,(250,0,0),(515,115),15)
    elif y[0][3]==2:
      pygame.draw.circle(screen,(0,250,0),(515,115),15)
    elif y[0][3]==3:
      pygame.draw.circle(screen,(0,0,250),(515,115),15)
    elif y[0][3]==4:
      pygame.draw.circle(screen,(250,250,0),(515,115),15)
  if y[1][3]==0:
    if y[1][0]==1:
      pygame.draw.circle(screen,(250,0,0),(500,185),25)
    elif y[1][0]==2:
      pygame.draw.circle(screen,(0,250,0),(500,185),25)
    elif y[1][0]==3:
      pygame.draw.circle(screen,(0,0,250),(500,185),25)
    elif y[1][0]==4:
      pygame.draw.circle(screen,(250,250,0),(500,185),25)
    if y[1][1]==1:
      pygame.draw.circle(screen,(250,0,0),(500,235),25)
    elif y[1][1]==2:
      pygame.draw.circle(screen,(0,250,0),(500,235),25)
    elif y[1][1]==3:
      pygame.draw.circle(screen,(0,0,250),(500,235),25)
    elif y[1][1]==4:
      pygame.draw.circle(screen,(250,250,0),(500,235),25)
  else:
    if y[1][0]==1:
      pygame.draw.circle(screen,(250,0,0),(485,195),15)
    elif y[1][0]==2:
      pygame.draw.circle(screen,(0,250,0),(485,195),15)
    elif y[1][0]==3:
      pygame.draw.circle(screen,(0,0,250),(485,195),15)
    elif y[1][0]==4:
      pygame.draw.circle(screen,(250,250,0),(485,195),15)
    if y[1][1]==1:
      pygame.draw.circle(screen,(250,0,0),(485,225),15)
    elif y[1][1]==2:
      pygame.draw.circle(screen,(0,250,0),(485,225),15)
    elif y[1][1]==3:
      pygame.draw.circle(screen,(0,0,250),(485,225),15)
    elif y[1][1]==4:
      pygame.draw.circle(screen,(250,250,0),(485,225),15)
    if y[1][2]==1:
      pygame.draw.circle(screen,(250,0,0),(515,195),15)
    elif y[1][2]==2:
      pygame.draw.circle(screen,(0,250,0),(515,195),15)
    elif y[1][2]==3:
      pygame.draw.circle(screen,(0,0,250),(515,195),15)
    elif y[1][2]==4:
      pygame.draw.circle(screen,(250,250,0),(515,195),15)
    if y[1][3]==1:
      pygame.draw.circle(screen,(250,0,0),(515,225),15)
    elif y[1][3]==2:
      pygame.draw.circle(screen,(0,250,0),(515,225),15)
    elif y[1][3]==3:
      pygame.draw.circle(screen,(0,0,250),(515,225),15)
    elif y[1][3]==4:
      pygame.draw.circle(screen,(250,250,0),(515,225),15)



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
    elif x[i]==5:
      pygame.draw.circle(screen,(20,180,250),(35+50*i,25),25)
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
    elif x[i]==5:
      pygame.draw.circle(screen,(20,180,250),(575+50*i,25),25)

def hyouji3_f(x,screen):
  for i in range(6):
    if x[i]==1:
     pygame.draw.circle(screen,(0,0,0),(50+50*i,15),15,2)
    elif x[i]==2:
      pygame.draw.circle(screen,(0,0,0),(50+50*i,15),25,2)
    elif x[i]==3:
      pygame.draw.circle(screen,(250,0,0),(50+50*i,15),25)
    elif x[i]==4:
      pygame.draw.circle(screen,(250,250,0),(50+50*i,15),25)
    elif x[i]==5:
      pygame.draw.circle(screen,(20,180,250),(50+50*i,15),25)
def hyouji3_f_2(x,screen):
  for i in range(6):
    if x[i]==1:
      pygame.draw.circle(screen,(0,0,0),(575+50*i,35),15,2)
    elif x[i]==2:
      pygame.draw.circle(screen,(0,0,0),(575+50*i,25),25,2)
    elif x[i]==3:
      pygame.draw.circle(screen,(250,0,0),(575+50*i,25),25)
    elif x[i]==4:
      pygame.draw.circle(screen,(250,250,0),(575+50*i,25),25)
    elif x[i]==5:
      pygame.draw.circle(screen,(20,180,250),(575+50*i,25),25)



def ojamahyouji(x,y,screen):
    y[0]=0
    y[1]=0
    y[2]=0
    y[3]=0
    y[4]=0
    y[5]=0
    x=x//70
    suisei=x//1080
    hoshi=(x % 1080)//180
    iwa=(x % 180)//30
    oo=(x % 30)//6
    syou=x % 6
    go0=suisei+hoshi
    go1=suisei+hoshi+iwa
    go2=suisei+hoshi+iwa+oo
    go3=suisei+hoshi+iwa+oo+syou
    if go0>6:
      go0=6
    if go1>6:
      go1=6
    if go2>6:
      go2=6
    if go3>6:
      go3=6
    for i in range(suisei):
      y[i]=5
    for i in range(suisei,go0):
      y[i]=4
    for i in range(go0,go1):
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
    suisei=x//1080
    hoshi=(x % 1080)//180
    iwa=(x % 180)//30
    oo=(x % 30)//6
    syou=x % 6
    go0=suisei+hoshi
    go1=suisei+hoshi+iwa
    go2=suisei+hoshi+iwa+oo
    go3=suisei+hoshi+iwa+oo+syou
    if go0>6:
      go0=6
    if go1>6:
      go1=6
    if go2>6:
      go2=6
    if go3>6:
      go3=6
    for i in range(suisei):
      y[i]=5
    for i in range(suisei,go0):
      y[i]=4
    for i in range(go0,go1):
      y[i]=3
    for i in range(go1,go2):
      y[i]=2
    for i in range(go2,go3):
      y[i]=1
    hyouji3(y,screen)


def ojamahyouji_f(x,y,screen):
    y[0]=0
    y[1]=0
    y[2]=0
    y[3]=0
    y[4]=0
    y[5]=0
    x=x//120
    suisei=x//1080
    hoshi=(x % 1080)//180
    iwa=(x % 180)//30
    oo=(x % 30)//6
    syou=x % 6
    go0=suisei+hoshi
    go1=suisei+hoshi+iwa
    go2=suisei+hoshi+iwa+oo
    go3=suisei+hoshi+iwa+oo+syou
    if go0>6:
      go0=6
    if go1>6:
      go1=6
    if go2>6:
      go2=6
    if go3>6:
      go3=6
    for i in range(suisei):
      y[i]=5
    for i in range(suisei,go0):
      y[i]=4
    for i in range(go0,go1):
      y[i]=3
    for i in range(go1,go2):
      y[i]=2
    for i in range(go2,go3):
      y[i]=1
    hyouji3_2(y,screen)
def ojamahyouji_f_2(x,y,screen):
    y[0]=0
    y[1]=0
    y[2]=0
    y[3]=0
    y[4]=0
    y[5]=0
    x=x//120
    suisei=x//1080
    hoshi=(x % 1080)//180
    iwa=(x % 180)//30
    oo=(x % 30)//6
    syou=x % 6
    go0=suisei+hoshi
    go1=suisei+hoshi+iwa
    go2=suisei+hoshi+iwa+oo
    go3=suisei+hoshi+iwa+oo+syou
    if go0>6:
      go0=6
    if go1>6:
      go1=6
    if go2>6:
      go2=6
    if go3>6:
      go3=6
    for i in range(suisei):
      y[i]=5
    for i in range(suisei,go0):
      y[i]=4
    for i in range(go0,go1):
      y[i]=3
    for i in range(go1,go2):
      y[i]=2
    for i in range(go2,go3):
      y[i]=1
    hyouji3(y,screen)


def ojamahyouji_ff(x,y,screen):
    y[0]=0
    y[1]=0
    y[2]=0
    y[3]=0
    y[4]=0
    y[5]=0
    x=x//120
    suisei=x//1080
    hoshi=(x % 1080)//180
    iwa=(x % 180)//30
    oo=(x % 30)//6
    syou=x % 6
    go0=suisei+hoshi
    go1=suisei+hoshi+iwa
    go2=suisei+hoshi+iwa+oo
    go3=suisei+hoshi+iwa+oo+syou
    if go0>6:
      go0=6
    if go1>6:
      go1=6
    if go2>6:
      go2=6
    if go3>6:
      go3=6
    for i in range(suisei):
      y[i]=5
    for i in range(suisei,go0):
      y[i]=4
    for i in range(go0,go1):
      y[i]=3
    for i in range(go1,go2):
      y[i]=2
    for i in range(go2,go3):
      y[i]=1
    hyouji3_f_2(y,screen)
def ojamahyouji_ff_2(x,y,screen):
    y[0]=0
    y[1]=0
    y[2]=0
    y[3]=0
    y[4]=0
    y[5]=0
    x=x//120
    suisei=x//1080
    hoshi=(x % 1080)//180
    iwa=(x % 180)//30
    oo=(x % 30)//6
    syou=x % 6
    go0=suisei+hoshi
    go1=suisei+hoshi+iwa
    go2=suisei+hoshi+iwa+oo
    go3=suisei+hoshi+iwa+oo+syou
    if go0>6:
      go0=6
    if go1>6:
      go1=6
    if go2>6:
      go2=6
    if go3>6:
      go3=6
    for i in range(suisei):
      y[i]=5
    for i in range(suisei,go0):
      y[i]=4
    for i in range(go0,go1):
      y[i]=3
    for i in range(go1,go2):
      y[i]=2
    for i in range(go2,go3):
      y[i]=1
    hyouji3_f(y,screen)

