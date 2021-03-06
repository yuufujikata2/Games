import pygame
from pygame.locals import *
import sys
import time
import copy
import random
import pickle
def allhyouji(haichi,haichi_2,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,i,zenkeshihyouji):
  screen.fill((250,250,250))
  pygame.draw.rect(screen,(0,0,0),Rect(10,50,300,600),5)
  pygame.draw.rect(screen,(0,0,0),Rect(330,50,70,230),5)
  pygame.draw.rect(screen,(0,0,0),Rect(550,50,300,600),5)
  pygame.draw.rect(screen,(0,0,0),Rect(460,50,70,230),5)
  font=pygame.font.Font(None,50)
  tokuten=font.render(str(counttotal2),False,(0,0,0))
  screen.blit(tokuten,(155,660))
  font_2=pygame.font.Font(None,50)
  tokuten_2=font_2.render(str(counttotal2_2),False,(0,0,0))
  screen.blit(tokuten_2,(695,660))
  if i!=0:
    font2=pygame.font.Font(None,50)
    chain=str(i)+"chain"
    rensahyouji=font2.render(chain,False,(250,0,0))
    screen.blit(rensahyouji,(5,660))
  if zenkeshihyouji==1:
    font_zen=pygame.font.Font(None,60)
    zen=font_zen.render("All Clear",False,(0,0,0))
    screen.blit(zen,(80,150))
  hyouji(haichi,screen)
  hyouji_2(haichi_2,screen)
  hyouji2(nexnex,screen)
  hyouji2_2(nexnex_2,screen)
  ojamahyouji(counttotal,ojama,screen)
  ojamahyouji_2(counttotal_2,ojama_2,screen)
  pygame.display.update()

def hyouji(x,screen):
  for i in range(12):
    for j in range(6):
      if x[i][j]==1:
        s=50*(11.5-i)
        s=int(s)
        k=j+0.5
        k=int(50*k)
        pygame.draw.circle(screen,(250,0,0),(k+10,s+50),25)
      elif x[i][j]==2:
        s=50*(11.5-i)
        s=int(s)
        k=j+0.5
        k=int(50*k)
        pygame.draw.circle(screen,(0,250,0),(k+10,s+50),25)
      elif x[i][j]==3:
        s=50*(11.5-i)
        s=int(s)
        k=j+0.5
        k=int(50*k)
        pygame.draw.circle(screen,(0,0,250),(k+10,s+50),25)
      elif x[i][j]==4:
        s=50*(11.5-i)
        s=int(s)
        k=j+0.5
        k=int(50*k)
        pygame.draw.circle(screen,(250,250,0),(k+10,s+50),25)
      elif x[i][j]==5:
        s=50*(11.5-i)
        s=int(s)
        k=j+0.5
        k=int(50*k)
        pygame.draw.circle(screen,(0,0,0),(k+10,s+50),25,1)
def hyouji_2(x,screen):
  for i in range(12):
    for j in range(6):
      if x[i][j]==1:
        s=50*(11.5-i)
        s=int(s)
        k=j+0.5
        k=int(50*k)
        pygame.draw.circle(screen,(250,0,0),(k+550,s+50),25)
      elif x[i][j]==2:
        s=50*(11.5-i)
        s=int(s)
        k=j+0.5
        k=int(50*k)
        pygame.draw.circle(screen,(0,250,0),(k+550,s+50),25)
      elif x[i][j]==3:
        s=50*(11.5-i)
        s=int(s)
        k=j+0.5
        k=int(50*k)
        pygame.draw.circle(screen,(0,0,250),(k+550,s+50),25)
      elif x[i][j]==4:
        s=50*(11.5-i)
        s=int(s)
        k=j+0.5
        k=int(50*k)
        pygame.draw.circle(screen,(250,250,0),(k+550,s+50),25)
      elif x[i][j]==5:
        s=50*(11.5-i)
        s=int(s)
        k=j+0.5
        k=int(50*k)
        pygame.draw.circle(screen,(0,0,0),(k+550,s+50),25,1)

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
    elif x[i]==5:
      pygame.draw.circle(screen,(0,0,0),(35+50*i,25),25)
      pygame.draw.circle(screen,(250,250,0),(35+50*i,25),25,2)
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
      pygame.draw.circle(screen,(0,0,0),(575+50*i,25),25)
      pygame.draw.circle(screen,(250,250,0),(575+50*i,25),25,2)

def ojamahyouji(x,y,screen):
    y[0]=0
    y[1]=0
    y[2]=0
    y[3]=0
    y[4]=0
    y[5]=0
    x=x//70
    tuki=x//1080
    hoshi=(x%1080)//180
    iwa=(x % 180)//30
    oo=(x % 30)//6
    syou=x % 6
    go0=tuki+hoshi
    go1=tuki+hoshi+iwa
    go2=tuki+hoshi+iwa+oo
    go3=tuki+hoshi+iwa+oo+syou
    if go0>6:
      go0=6
    if go1>6:
      go1=6
    if go2>6:
      go2=6
    if go3>6:
      go3=6
    for i in range(tuki):
      y[i]=5
    for i in range(tuki,go0):
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
    tuki=x//1080
    hoshi=(x%1080)//180
    iwa=(x % 180)//30
    oo=(x % 30)//6
    syou=x % 6
    go0=tuki+hoshi
    go1=tuki+hoshi+iwa
    go2=tuki+hoshi+iwa+oo
    go3=tuki+hoshi+iwa+oo+syou
    if go0>6:
      go0=6
    if go1>6:
      go1=6
    if go2>6:
      go2=6
    if go3>6:
      go3=6
    for i in range(tuki):
      y[i]=5
    for i in range(tuki,go0):
      y[i]=4
    for i in range(go0,go1):
      y[i]=3
    for i in range(go1,go2):
      y[i]=2
    for i in range(go2,go3):
      y[i]=1
    hyouji3(y,screen)


def ojamarakka(haichi,haichi_2,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,zenkeshihyouji):
  while counttotal>2100:
    haichi_2.append([0,0,0,0,0,0])
    haichi_2.append([0,0,0,0,0,0])
    haichi_2.append([0,0,0,0,0,0])
    haichi_2.append([0,0,0,0,0,0])
    haichi_2.append([0,0,0,0,0,0])
    counttotal-=2100
    ojamahyouji(counttotal,ojama,screen)
    allhyouji(haichi,haichi_2,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,0,zenkeshihyouji)
    for j in range(13,18):
      for i in range(6):
        haichi_2[j][i]=5
    sokurakka_2(haichi,haichi_2,18,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,zenkeshihyouji)
    haichi_2.pop(17)
    haichi_2.pop(16)
    haichi_2.pop(15)
    haichi_2.pop(14)
    haichi_2.pop(13)
  ojamahyouji(counttotal,ojama,screen)
  allhyouji(haichi,haichi_2,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,0,zenkeshihyouji)
  time.sleep(1)
  haichi_2.append([0,0,0,0,0,0])
  haichi_2.append([0,0,0,0,0,0])
  haichi_2.append([0,0,0,0,0,0])
  haichi_2.append([0,0,0,0,0,0])
  haichi_2.append([0,0,0,0,0,0])
  y1=counttotal//70
  y2=counttotal%70
  if y1>24:
    for j in range(13,17):
      for i in range(6):
        haichi_2[j][i]=5
    o=random.sample(range(6),6)
    for i in range(y1-24):
      haichi_2[17][o[i]]=5
  elif y1>18:
    for j in range(13,16):
      for i in range(6):
        haichi_2[j][i]=5
    o=random.sample(range(6),6)
    for i in range(y1-18):
      haichi_2[16][o[i]]=5
  elif y1>12:
    for j in range(13,15):
      for i in range(6):
        haichi_2[j][i]=5
    o=random.sample(range(6),6)
    for i in range(y1-12):
      haichi_2[15][o[i]]=5
  elif y1>6:
    for j in range(13,14):
      for i in range(6):
        haichi_2[j][i]=5
    o=random.sample(range(6),6)
    for i in range(y1-6):
      haichi_2[14][o[i]]=5
  else:
    o=random.sample(range(6),6)
    for i in range(y1):
      haichi_2[13][o[i]]=5
  ojamahyouji(0,ojama,screen)
  allhyouji(haichi,haichi_2,nexnex,nexnex_2,ojama,ojama_2,0,counttotal_2,counttotal2,counttotal2_2,screen,0,zenkeshihyouji)
  sokurakka_2(haichi,haichi_2,18,nexnex,nexnex_2,ojama,ojama_2,0,counttotal_2,counttotal2,counttotal2_2,screen,zenkeshihyouji)
  haichi_2.pop(17)
  haichi_2.pop(16)
  haichi_2.pop(15)
  haichi_2.pop(14)
  haichi_2.pop(13)
  return y2

def ichimasurakka(x,y):
  count=0 
  for j in range(1,y):
    for i in range(6):
      if x[j][i]!=0 and x[j-1][i]==0:
        x[j-1][i]=x[j][i]
        x[j][i]=0
        count+=1
  return count 
def rakka(haichi,haichi_2,y,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,zenkeshihyouji):
  count2=0
  while True:
    count=0
    for j in range(1,y):
      for i in range(6):
        if haichi[j][i]!=0 and haichi[j-1][i]==0:
          count+=1
          haichi[j-1][i]=haichi[j][i]
          haichi[j][i]=0
    allhyouji(haichi,haichi_2,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,0,zenkeshihyouji)
    count2+=1
    if count==0:
      break
    time.sleep(0.2)
  return count2
def rakka_chigiri(haichi,haichi_2,y,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,zenkeshihyouji):
  count2=0
  while True:
    count=0
    for j in range(1,y):
      for i in range(6):
        if haichi[j][i]!=0 and haichi[j-1][i]==0:
          count+=1
          haichi[j-1][i]=haichi[j][i]
          haichi[j][i]=0
    allhyouji(haichi,haichi_2,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,0,zenkeshihyouji)
    count2+=1
    if count==0:
      break
    time.sleep(0.4)
  return count2
def sokurakka(haichi,haichi_2,y,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,zenkeshihyoji):
  count2=0
  while True:
    count=0
    for j in range(1,y):
      for i in range(6):
        if haichi[j][i]!=0 and haichi[j-1][i]==0:
          count+=1
          haichi[j-1][i]=haichi[j][i]
          haichi[j][i]=0
    count2+=1
    allhyouji(haichi,haichi_2,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,0,zenkeshihyoji)
    if count==0:
      break
  time.sleep(0.4)
  return count2
def sokurakka_2(haichi,haichi_2,y,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,zenkeshihyouji):
  count2=0
  while True:
    count=0
    for j in range(1,y):
      for i in range(6):
        if haichi_2[j][i]!=0 and haichi_2[j-1][i]==0:
          count+=1
          haichi_2[j-1][i]=haichi_2[j][i]
          haichi_2[j][i]=0
    count2+=1
    allhyouji(haichi,haichi_2,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,0,zenkeshihyouji)
    if count==0:
      break
  time.sleep(0.4)
  return count2

def renketu(x,i,j):
  a=x[j][i]
  if a==0 or a==5 or a==11 or a==12 or a==13 or a==14:
    return 1
  if x[j][i]==1:
    x[j][i]=11
  elif x[j][i]==2:
    x[j][i]=12
  elif x[j][i]==3:
    x[j][i]=13
  elif x[j][i]==4:
    x[j][i]=14
  if i!=5:
    if a==x[j][i+1] :
      renketu(x,i+1,j)
    elif x[j][i+1]==5:
      x[j][i+1]=15
  if i!=0:
    if a==x[j][i-1] :
      renketu(x,i-1,j)
    elif x[j][i-1]==5:
      x[j][i-1]=15
  if j!=11:
    if a==x[j+1][i]:
      renketu(x,i,j+1)
    elif x[j+1][i]==5:
      x[j+1][i]=15
  if j!=0:
    if a==x[j-1][i]:
      renketu(x,i,j-1)
    elif x[j-1][i]==5:
      x[j-1][i]=15
  return 1
def renketukeshi(x):
  count3=0
  count4=0
  count6=0
  irosuu=[0,0,0,0]
  for j in range(12):
    for i in range(6):
      count21=0
      count22=0
      count23=0
      count24=0
      count31=0
      y=copy.deepcopy(x)
      renketu(x,i,j)
      for l in range(12):
        for k in range(6):
          if x[l][k]==11:
            count21+=1
          elif x[l][k]==12:
            count22+=1
          elif x[l][k]==13:
            count23+=1
          elif x[l][k]==14:
            count24+=1
      if count21>=4 or count22>=4 or count23>=4 or count24>=4:
        if count21>=4:
          irosuu[0]=1
        if count22>=4:
          irosuu[1]=1
        if count23>=4:
          irosuu[2]=1
        if count24>=4:
          irosuu[3]=1
        count31=count21+count22+count23+count24
        count3=count3+count21+count22+count23+count24
        if count31==4:
          count5=0
        elif count31==5:
          count5=2
        elif count31==6:
          count5=3
        elif count31==7:
          count5=4
        elif count31==8:
          count5=5
        elif count31==9:
          count5=6
        elif count31==10:
          count5=7
        elif count31>=11:
          count5=10
        count4+=count5
        for l in range(12):
          for k in range(6):
            if x[l][k]==11 or x[l][k]==12 or x[l][k]==13 or x[l][k]==14 or x[l][k]==15:
              x[l][k]=0
      else:
        for l in range(12):
          for k in range(6):
            if x[l][k]==11 or x[l][k]==12 or x[l][k]==13 or x[l][k]==14 or x[l][k]==15:
              x[l][k]=y[l][k]
  count7=irosuu[0]+irosuu[1]+irosuu[2]+irosuu[3]
  if count7==1:
    count6=0
  if count7==2:
    count6=3
  if count7==3:
    count6=6
  if count7==4:
    count6=12
  return count3,count4,count6
def rensa(x,x_2,y,y_2,z,z_2,haichi2,nexnex2,puyo1,puyo2,i,screen):
  i+=1
  global counttotal,counttotal_2,counttotal2,counttotal2_2,zenkeshihyouji,counttotal_r
  count=0
  if i==1:
    count=0
  elif i==2:
    count=8
  elif i==3:
    count=16
  elif i==4:
    count=32
  elif i==5:
    count=64
  elif i==6:
    count=96
  elif i==7:
    count=128
  elif i==8:
    count=160
  elif i==9:
    count=192
  elif i==10:
    count=224
  elif i==11:
    count=256
  elif i==12:
    count=288
  elif i==13:
    count=320
  elif i==14:
    count=352
  elif i==15:
    count=384
  elif i==16:
    count=416
  elif i==17:
    count=448
  elif i==18:
    count=480
  elif i==19:
    count=512
  j=renketukeshi(x)
  k=count+j[1]+j[2]
  #print(count)
  #print(j[0])
  #print(j[1])
  #print(j[2])
  '''
  for event in pygame.event.get():
    if event.type==KEYDOWN:
      if event.key==K_p:
        pickle_haichi=open('haichi.binaryfile','wb')
        pickle.dump(haichi2,pickle_haichi)
        pickle_haichi.close
        pickle_nexnex=open('nexnex.binaryfile','wb')
        pickle.dump(nexnex2,pickle_nexnex)
        pickle_nexnex.close
        pickle_puyo1=open('puyo1.binaryfile','wb')
        pickle.dump(puyo1,pickle_puyo1)
        pickle_puyo1.close
        pickle_puyo2=open('puyo2.binaryfile','wb')
        pickle.dump(puyo2,pickle_puyo2)
        pickle_puyo2.close
        pygame.quit()
        sys.exit()
  '''
  if k==0:
    k=1 
  counttotal+=j[0]*k*10
  counttotal2+=j[0]*k*10
  if j[0]!=0 and zenkeshihyouji==1:
    counttotal+=2100
    zenkeshihyouji=0
  if j[0]!=0 and counttotal_r!=0:
    counttotal+=counttotal_r
    counttotal_r=0
  allhyouji(x,x_2,y,y_2,z,z_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,i,zenkeshihyouji)
  if j[0]!=0:
    time.sleep(0.8)
  aa=rakka(x,x_2,13,y,y_2,z,z_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,zenkeshihyouji)
 # print("counttotal")
#  print(counttotal)
  if aa==1:
    return 1
  rensa(x,x_2,y,y_2,z,z_2,haichi2,nexnex2,puyo1,puyo2,i,screen)
def idouhantei(haichi2,puyo1,puyo2,x):
  if x==1 and puyo1[1]!=0 and puyo2[1]!=0:
    if haichi2[puyo1[2]][puyo1[1]-1]==0 and haichi2[puyo2[2]][puyo2[1]-1]==0 :
      return 1
  elif x==2 and  puyo1[1]!=5 and puyo2[1]!=5:
    if haichi2[puyo1[2]][puyo1[1]+1]==0 and haichi2[puyo2[2]][puyo2[1]+1]==0:
      return 1
  elif x==3 and puyo1[2]!=0 and puyo2[2]!=0:
    if  haichi2[puyo1[2]-1][puyo1[1]]==0 and haichi2[puyo2[2]-1][puyo2[1]]==0:
      return 1
  return 0
def kaitenhantei(haichi2,puyo1,puyo2,x):
  if x==1:
    if puyo1[2]-1==puyo2[2]:
      if puyo1[1]==0:
        if haichi2[puyo2[2]][puyo2[1]+1]==0:
          return 5
        else:
          return 7
      elif puyo1[1]==5:
        if haichi2[puyo2[2]][puyo2[1]-1]==0:
          return 1
        else:
          return 7
      else:
        if haichi2[puyo2[2]][puyo2[1]-1]==0:
          return 1
        elif haichi2[puyo2[2]][puyo2[1]+1]==0:
          return 5
        else:
          return 7
    elif puyo1[1]+1==puyo2[1]:
      if puyo1[2]==0:
        return 10
      elif puyo1[2]==12:
        return 0
      else:
        if haichi2[puyo2[2]-1][puyo2[1]]==0:
          return 2
        else:
          return 10
    elif puyo1[2]+1==puyo2[2]:
      if puyo1[1]==0:
        if haichi2[puyo2[2]][puyo2[1]+1]==0:
          return 3
        else:
          return 8
      elif puyo1[1]==5:
        if haichi2[puyo1[2]][puyo1[1]-1]==0:
          return 6
        else:
          return 8
      else:
        if haichi2[puyo2[2]][puyo2[1]+1]==0:
          return 3
        elif haichi2[puyo1[2]][puyo1[1]-1]==0:
          return 6
        else:
          return 8
    elif puyo1[1]-1==puyo2[1]:
      return 4
  if x==2:
    if puyo1[2]-1==puyo2[2]:
      if puyo1[1]==0:
        if haichi2[puyo2[2]][puyo2[1]+1]==0:
          return 1
        else:
          return 7
      elif puyo1[1]==5:
        if haichi2[puyo2[2]][puyo2[1]-1]==0:
          return 5
        else:
          return 7
      else:
        if haichi2[puyo2[2]][puyo2[1]+1]==0:
          return 1
        elif haichi2[puyo2[2]][puyo2[1]-1]==0:
          return 5
        else:
          return 7
    elif puyo1[1]-1==puyo2[1]:
      if puyo1[2]==0:
        return 10
      elif puyo1[2]==12:
        return 0
      else:
        if haichi2[puyo2[2]-1][puyo2[1]]==0:
          return 2
        else:
          return 10
    elif puyo1[2]+1==puyo2[2]:
      if puyo1[1]==0:
        if haichi2[puyo1[2]][puyo1[1]+1]==0:
          return 6
        else:
          return 8
      elif puyo1[1]==5:
        if haichi2[puyo2[2]][puyo2[1]-1]==0:
          return 3
        else:
          return 8
      else:
        if haichi2[puyo2[2]][puyo2[1]-1]==0:
          return 3
        elif haichi2[puyo1[2]][puyo1[1]+1]==0:
          return 6
        else:
          return 8
    elif puyo1[1]+1==puyo2[1]:
      return 4
    '''
    if puyo1[1]!=0:
      if puyo1[2]-1==puyo2[2]and haichi2[puyo1[2]][puyo1[1]-1]==0 and haichi2[puyo2[2]][puyo2[1]-1]==0:
        return 1
      if puyo1[1]!=5 and puyo1[2]-1==puyo2[2] and haichi2[puyo1[2]][puyo1[1]-1]!=0  and haichi2[puyo2[2]][puyo2[1]+1]==0:
        return 5
    if puyo1[2]!=0:
      if puyo1[1]+1==puyo2[1] and haichi2[puyo1[2]-1][puyo1[1]]==0 and haichi2[puyo1[2]-1][puyo2[1]]==0:
        return 2
    if puyo1[1]!=5:
      if puyo1[2]+1==puyo2[2] and haichi2[puyo1[2]][puyo1[1]+1]==0 and haichi2[puyo2[2]][puyo2[1]+1]==0:
        return 3
      if puyo1[1]!=0 and puyo1[2]+1==puyo2[2] and haichi2[puyo2[2]][puyo2[1]+1]!=0 and haichi2[puyo2[2]][puyo2[1]-1]==0: 
        return 6
    if puyo1[1]-1==puyo2[1] and haichi2[puyo1[2]+1][puyo1[1]]==0 and haichi2[puyo2[2]+1][puyo2[1]]==0:
        return 4
    if puyo1[1]==0:
      if puyo1[2]-1==puyo2[2] and haichi2[puyo2[2]][puyo1[1]+1]==0:
        return 5 
    if puyo1[1]==5:
      if puyo1[2]+1==puyo2[2]and haichi2[puyo1[2]][puyo1[1]-1]==0:
        return 6
    if puyo1[1]==0 and puyo2[2]!=0 and puyo1[2]-1==puyo2[2] and  haichi2[puyo1[2]][puyo1[1]+1]!=0:
      return 7
    if puyo1[1]!=0 and puyo2[2]!=0 and puyo1[2]-1==puyo2[2]:
      if haichi2[puyo1[2]][puyo1[1]-1]!=0 and haichi2[puyo1[2]][puyo1[1]+1]!=0:
        return 7
    if puyo1[1]==5 and puyo1[2]+1==puyo2[2] and haichi2[puyo2[2]][puyo2[1]-1]!=0:
      return 8
    if puyo1[1]!=5 and puyo1[2]+1==puyo2[2]:
      if puyo1[1]!=0 and haichi2[puyo2[2]][puyo2[1]-1]!=0 and haichi2[puyo2[2]][puyo2[1]+1]!=0:
        return 8
      if puyo1[1]==0 and haichi2[puyo2[2]][puyo2[1]+1]!=0:
        return 8
    '''
  '''
  if x==2:
    if puyo1[1]!=5:
      if puyo1[2]-1==puyo2[2]and haichi2[puyo1[2]][puyo1[1]+1]==0 and haichi2[puyo2[2]][puyo2[1]+1]==0: 
        return 1
    if puyo1[2]!=0:
      if puyo1[1]-1==puyo2[1] and haichi2[puyo1[2]-1][puyo1[1]]==0 and haichi2[puyo1[2]-1][puyo2[1]]==0: 
        return 2
    if puyo1[1]!=0:
      if puyo1[2]+1==puyo2[2] and haichi2[puyo1[2]][puyo1[1]-1]==0 and haichi2[puyo2[2]][puyo2[1]-1]==0:  
        return 3
    if puyo1[1]+1==puyo2[1] and haichi2[puyo1[2]+1][puyo1[1]]==0 and haichi2[puyo2[2]+1][puyo2[1]]==0:
      return 4
  '''
  return 0

counttotal=0
counttotal2=0
counttotal_2=0
counttotal2_2=0
counttotal_r=0
zenkeshihyouji=0
def main():
  global counttotal,counttotal2,counttotal_2,counttotal2_2,zenkeshihyouji,counttotal_r
  haichi=[[0 for i in range(6)] for j in range(14)]
  haichi2=[[0 for i in range(6)] for j in range(14)]
  haichi_2=[[0 for i in range(6)] for j in range(14)]
  ojama=[0,0,0,0,0,0]
  ojama_2=[0,0,0,0,0,0]
  nexnex=[0,0,0,0]
  nexnex_2=[0,0,0,0]
  nexnex_2[0]=1
  nexnex_2[1]=1
  nexnex_2[2]=2
  nexnex_2[3]=1
  puyo1=[0,0,0]
  puyo1_2=[0,0,0]
  puyo2=[0,0,0]
  puyo2_2=[0,0,0]
  tumosyote=[random.randint(1,3) for i in range(4)]
  tumo=[0 for i in range(256)]
  for i in range(256):
    if i<=63:
      tumo[i]=1
    elif i<=127:
      tumo[i]=2
    elif i<=191:
      tumo[i]=3
    else:
      tumo[i]=4
  random.shuffle(tumo)
  n1=tumosyote[0]
  n2=tumosyote[1]
  n3=tumosyote[2]
  n4=tumosyote[3]
  tumo_c=0
  nexnex[0]=n1
  nexnex[1]=n2
  nexnex[2]=n3
  nexnex[3]=n4
  pygame.init()
  screen=pygame.display.set_mode((860,700))
  pygame.display.set_caption("tokopuyo")
  clock=pygame.time.Clock()
  allhyouji(haichi,haichi_2,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,0,zenkeshihyouji)
  time.sleep(2)
  while True:
    puyo12=copy.deepcopy(puyo1)
    puyo22=copy.deepcopy(puyo2)
    puyo1[0]=n1
    puyo2[0]=n2
    n1=n3
    n2=n4
    n3=tumo[tumo_c]
    n4=tumo[tumo_c+1]
    tumo_c+=2
    if tumo_c==256:
      tumo_c=0
    nexnex2=copy.deepcopy(nexnex)
    nexnex[0]=n1
    nexnex[1]=n2
    nexnex[2]=n3
    nexnex[3]=n4
    haichi3=copy.deepcopy(haichi2)
    haichi2=copy.deepcopy(haichi)
    puyo1[1]=2
    puyo1[2]=12
    puyo2[1]=2
    puyo2[2]=11
    haichi[12][2]=puyo1[0]
    haichi[11][2]=puyo2[0]
    hidari_c=0
    migi_c=0
    idou_c=0
    kaiten=0
    setticount=0
    posecount=0
    surinukecount=0
    surinukecount2=0
    suri=-11
    suri2=-11
    rakkab_c=0
    while True:
      clock.tick(60)
      surinukecount+=1
      surinukecount2+=1
      allhyouji(haichi,haichi_2,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,0,zenkeshihyouji)
      haichi[puyo1[2]][puyo1[1]]=0
      haichi[puyo2[2]][puyo2[1]]=0
      if hidari_c>=8:
        idou=idouhantei(haichi2,puyo1,puyo2,1)
        if idou==1:
          puyo1[1]-=1
          puyo2[1]-=1
        hidari_c=0
      if migi_c>=8:
        idou=idouhantei(haichi2,puyo1,puyo2,2)
        if idou==1:
          puyo1[1]+=1
          puyo2[1]+=1
        migi_c=0
      pygame.event.pump()
      pressed_key=pygame.key.get_pressed()
      if pressed_key[K_LEFT]:
        hidari_c+=1
      if pressed_key[K_RIGHT]:
        migi_c+=1
      if pressed_key[K_DOWN]:
        idou=idouhantei(haichi2,puyo1,puyo2,3)
        if idou==1:
          idou_c+=10
          rakkab_c+=1
        elif idou==0:
          setticount+=50
      for event in pygame.event.get():
        if event.type==QUIT:
          pygame.quit()
          sys.exit()
          
        if event.type==KEYDOWN:
          '''
          if event.key==K_LEFT:
#            if puyo1[1]<0:
#              puyo1[1]=0
#            if puyo2[1]<0:
#              puyo2[1]=0
            idou=idouhantei(haichi2,puyo1,puyo2,1)
            if idou==1:
              puyo1[1]-=1
              puyo2[1]-=1
          if event.key==K_RIGHT:
 #           if puyo1[1]>5:
#              puyo1[1]=5
#            if puyo2[1]>5:
#              puyo2[1]=5
            idou=idouhantei(haichi2,puyo1,puyo2,2)
            if idou==1:
              puyo1[1]+=1
              puyo2[1]+=1
          if event.key==K_DOWN:
            idou=idouhantei(haichi2,puyo1,puyo2,3)
            if idou==1:
              puyo1[2]-=1
              puyo2[2]-=1
            haichi[puyo1[2]][puyo1[1]]=puyo1[0]
            haichi[puyo2[2]][puyo2[1]]=puyo2[0]
            if haichi[11][2]!=0:
              pygame.quit()
              sys.exit()
            soku2+=1
          if event.key==K_UP:
            haichi[puyo1[2]][puyo1[1]]=puyo1[0]
            haichi[puyo2[2]][puyo2[1]]=puyo2[0]
            sokurakka(haichi,haichi_2,13,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,zenkeshihyouji)

            soku+=1
          
            if haichi[11][2]!=0:
              pygame.quit()
              sys.exit()
          '''
          if event.key==K_a:
            kaiten=kaitenhantei(haichi2,puyo1,puyo2,1)
            if kaiten==1:
              puyo1[1]-=1
              puyo1[2]-=1
            elif kaiten==2:
              puyo1[1]+=1
              puyo1[2]-=1
            elif kaiten==3:
              puyo1[1]+=1
              puyo1[2]+=1
            elif kaiten==4:
              puyo1[1]-=1
              puyo1[2]+=1
            elif kaiten==5:
              puyo1[2]-=1
              puyo2[1]+=1
            elif kaiten==6:
              puyo1[2]+=1
              puyo2[1]-=1
            elif kaiten==7:
              if surinukecount-suri<30:
                puyo1[2]-=1
                puyo2[2]+=1
              suri=surinukecount
            elif kaiten==8:
              if surinukecount2-suri2<30:
                puyo1[2]+=1
                puyo2[2]-=1
              suri2=surinukecount
            elif kaiten==10:
              puyo1[1]+=1
              puyo2[2]+=1
          if event.key==K_f:
            kaiten=kaitenhantei(haichi2,puyo1,puyo2,2)
            if kaiten==1:
              puyo1[1]+=1
              puyo1[2]-=1
            elif kaiten==2:
              puyo1[1]-=1
              puyo1[2]-=1
            elif kaiten==3:
              puyo1[1]-=1
              puyo1[2]+=1
            elif kaiten==4:
              puyo1[1]+=1
              puyo1[2]+=1
            elif kaiten==5:
              puyo1[2]-=1
              puyo2[1]-=1
            elif kaiten==6:
              puyo1[2]+=1
              puyo2[1]+=1
            elif kaiten==7:
              if surinukecount-suri<30:
                puyo1[2]-=1
                puyo2[2]+=1
              suri=surinukecount
            elif kaiten==8:
              if surinukecount2-suri2<30:
                puyo1[2]+=1
                puyo2[2]-=1
              suri2=surinukecount2
            elif kaiten==10:
              puyo1[1]-=1
              puyo2[2]+=1
          if event.key==K_h:
            pickle_haichi=open('haichi.binaryfile','wb')
            pickle.dump(haichi2,pickle_haichi)
            pickle_haichi.close
            pickle_nexnex=open('nexnex.binaryfile','wb')
            pickle.dump(nexnex,pickle_nexnex)
            pickle_nexnex.close
            pickle_puyo1=open('puyo1.binaryfile','wb')
            pickle.dump(puyo1,pickle_puyo1)
            pickle_puyo1.close
            pickle_puyo2=open('puyo2.binaryfile','wb')
            pickle.dump(puyo2,pickle_puyo2)
            pickle_puyo2.close
          if event.key==K_j:
            pickle_haichi=open('haichi.binaryfile','wb')
            pickle.dump(haichi3,pickle_haichi)
            pickle_haichi.close
            pickle_nexnex=open('nexnex.binaryfile','wb')
            pickle.dump(nexnex2,pickle_nexnex)
            pickle_nexnex.close
            pickle_puyo1=open('puyo1.binaryfile','wb')
            pickle.dump(puyo12,pickle_puyo1)
            pickle_puyo1.close
            pickle_puyo2=open('puyo2.binaryfile','wb')
            pickle.dump(puyo22,pickle_puyo2)
            pickle_puyo2.close
            tumo_h=tumo_c
          if event.key==K_k:
            pickle_haichi=open('haichi.binaryfile','rb')
            haichi=pickle.load(pickle_haichi)
            haichi2=copy.deepcopy(haichi)
            pickle_haichi.close
            pickle_nexnex=open('nexnex.binaryfile','rb')
            nexnex=pickle.load(pickle_nexnex)
            pickle_nexnex.close
            pickle_puyo1=open('puyo1.binaryfile','rb')
            puyo1=pickle.load(pickle_puyo1)
            pickle_puyo1.close
            pickle_puyo2=open('puyo2.binaryfile','rb')
            puyo2=pickle.load(pickle_puyo2)
            pickle_puyo2.close
            tumo_c=tumo_h-2
            puyo1[1]=2
            puyo1[2]=12
            puyo2[1]=2
            puyo2[2]=11
            n1=nexnex[0]
            n2=nexnex[1]
            n3=nexnex[2]
            n4=nexnex[3]
          if event.key==K_e:
            if posecount==0:
              posecount=1
            else:
              posecount=0
      '''
      if soku!=0:
        break
      if soku2!=0:
        continue
      '''
      if posecount==0:
        idou=idouhantei(haichi2,puyo1,puyo2,3)
        if idou==1:
          idou_c+=1
          if setticount>60:
            idou_c+=60
        if idou==0:
          setticount+=1
        if idou_c>=60:
          puyo1[2]-=1
          puyo2[2]-=1
          idou_c=0
          setticount=0
          if rakkab_c!=0:
            counttotal_r+=1
            counttotal2+=1
            rakkab_c=0
      haichi[puyo1[2]][puyo1[1]]=puyo1[0]
      haichi[puyo2[2]][puyo2[1]]=puyo2[0]
      if setticount>=60:
        rakka_chigiri(haichi,haichi_2,13,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,zenkeshihyouji)
        time.sleep(0.4)
        break 
    countcheck=counttotal2
    rensa(haichi,haichi_2,nexnex,nexnex_2,ojama,ojama_2,haichi2,nexnex,puyo1,puyo2,0,screen)
    pygame.event.clear()
    if haichi[11][2]!=0 :
      pygame.quit()
      sys.exit()
    allhyouji(haichi,haichi_2,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,0,zenkeshihyouji)
    if countcheck!=counttotal2:
      allhyouji(haichi,haichi_2,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,0,zenkeshihyouji)
      zenkeshicount=0
      for i in range(13):
        for j in range(6):
          if haichi[i][j]!=0:
            zenkeshicount+=1
      if zenkeshicount==0:
        zenkeshihyouji=1
      if counttotal>=70:
        counttotal=ojamarakka(haichi,haichi_2,nexnex,nexnex_2,ojama,ojama_2,counttotal,counttotal_2,counttotal2,counttotal2_2,screen,zenkeshihyouji)
#    print(counttotal)
#    print (counttotal2)
    for event in pygame.event.get():
      if event.type==QUIT:
        pygame.quit()
        sys.exit()
if __name__=="__main__":
  main()
