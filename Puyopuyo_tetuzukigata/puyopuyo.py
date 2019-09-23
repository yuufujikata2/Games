import pygame
from pygame.locals import *
import sys
import time
import copy
import random
import pylab
import numpy as np
import pickle
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
    hyouji3(y,screen)
def ichimasurakka(x,y):
  count=0 
  for j in range(1,y):
    for i in range(6):
      if x[j][i]!=0 and x[j-1][i]==0:
        x[j-1][i]=x[j][i]
        x[j][i]=0
        count+=1
  return count 
def rakka(x,y,nexnex,ojama,counttotal,screen):
  global counttotal2
  count2=0
  while True:
    count=0
    for j in range(1,y):
      for i in range(6):
        if x[j][i]!=0 and x[j-1][i]==0:
          count+=1
          x[j-1][i]=x[j][i]
          x[j][i]=0
    screen.fill((250,250,250))
    pygame.draw.rect(screen,(0,0,0),Rect(10,50,300,600),5)
    pygame.draw.rect(screen,(0,0,0),Rect(330,50,70,230),5)
    font=pygame.font.Font(None,50)
    tokuten=font.render(str(counttotal2),False,(0,0,0))
    screen.blit(tokuten,(155,660))
    hyouji(x,screen)
    hyouji2(nexnex,screen)
    ojamahyouji(counttotal,ojama,screen)
    pygame.display.update()
    count2+=1
    if count==0:
      break
    time.sleep(0.8)
  return count2
def sokurakka(x,y,nexnex,ojama,counttotal,screen):
  global counttotal2
  count2=0
  while True:
    count=0
    for j in range(1,y):
      for i in range(6):
        if x[j][i]!=0 and x[j-1][i]==0:
          count+=1
          x[j-1][i]=x[j][i]
          x[j][i]=0
    count2+=1
    screen.fill((250,250,250))
    pygame.draw.rect(screen,(0,0,0),Rect(10,50,300,600),5)
    pygame.draw.rect(screen,(0,0,0),Rect(330,50,70,230),5)
    font=pygame.font.Font(None,50)
    tokuten=font.render(str(counttotal2),False,(0,0,0))
    screen.blit(tokuten,(155,660))
    hyouji(x,screen)
    hyouji2(nexnex,screen)
    ojamahyouji(counttotal,ojama,screen)
    pygame.display.update()
    if count==0:
      break
  time.sleep(0.8)
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
def rensa(x,y,z,i,screen):
  i+=1
  global counttotal,counttotal2
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
  if k==0:
    k=1 
  counttotal+=j[0]*k*10
  counttotal2+=j[0]*k*10
  screen.fill((250,250,250))
  pygame.draw.rect(screen,(0,0,0),Rect(10,50,300,600),5)
  pygame.draw.rect(screen,(0,0,0),Rect(330,50,70,230),5)
  font=pygame.font.Font(None,50)
  tokuten=font.render(str(counttotal2),False,(0,0,0))
  screen.blit(tokuten,(155,660))
  font2=pygame.font.Font(None,50)
  chain=str(i)+"chain"
  rensahyouji=font2.render(chain,False,(250,0,0))
  screen.blit(rensahyouji,(5,660))
  hyouji(x,screen)
  hyouji2(y,screen)
  ojamahyouji(counttotal,z,screen)
  pygame.display.update()
  if j[0]!=0:
    time.sleep(0.8)
  aa=rakka(x,13,y,z,counttotal,screen)
 # print("counttotal")
#  print(counttotal)
  if aa==1:
    return 1
  rensa(x,y,z,i,screen)
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
    if puyo1[1]!=0:
      if puyo1[2]-1==puyo2[2]and haichi2[puyo1[2]][puyo1[1]-1]==0 and haichi2[puyo2[2]][puyo2[1]-1]==0:
        return 1
    if puyo1[2]!=0:
      if puyo1[1]+1==puyo2[1] and haichi2[puyo1[2]-1][puyo1[1]]==0 and haichi2[puyo1[2]-1][puyo2[1]]==0:
        return 2
    if puyo1[1]!=5:
      if puyo1[2]+1==puyo2[2] and haichi2[puyo1[2]][puyo1[1]+1]==0 and haichi2[puyo2[2]][puyo2[1]+1]==0:
        return 3
    if puyo1[1]-1==puyo2[1] and haichi2[puyo1[2]+1][puyo1[1]]==0 and haichi2[puyo2[2]+1][puyo2[1]]==0:
      return 4
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
  return 0

counttotal=0
counttotal2=0
def main():
  global counttotal,counttotal2
  haichi=[[0 for i in range(6)] for j in range(13)]
  ojama=[0,0,0,0,0,0]
  nexnex=[0,0,0,0]
  puyo1=[0,0,0]
  puyo2=[0,0,0]
  pygame.init()
  screen=pygame.display.set_mode((860,700))
  pygame.display.set_caption("tokopuyo")
  n1=random.randint(1,3)
  n2=random.randint(1,3)
  n3=random.randint(1,3)
  n4=random.randint(1,3)
  nexnex[0]=n1
  nexnex[1]=n2
  nexnex[2]=n3
  nexnex[3]=n4
  screen.fill((250,250,250))
  pygame.draw.rect(screen,(0,0,0),Rect(10,50,300,600),5)
  pygame.draw.rect(screen,(0,0,0),Rect(330,50,70,230),5)
  hyouji(haichi,screen)
  hyouji2(nexnex,screen)
  ojamahyouji(0,ojama,screen)
  pygame.display.update()
  time.sleep(2)
  while(1):
    puyo1[0]=n1
    puyo2[0]=n2
    n1=n3
    n2=n4
    n3=random.randint(1,4)
    n4=random.randint(1,4)
    nexnex[0]=n1
    nexnex[1]=n2
    nexnex[2]=n3
    nexnex[3]=n4
    haichi2=copy.deepcopy(haichi)
    puyo1[1]=2
    puyo1[2]=12
    puyo2[1]=2
    puyo2[2]=11
    haichi[12][2]=puyo1[0]
    haichi[11][2]=puyo2[0]
    while(1):
      soku=0
      soku2=0
      screen.fill((250,250,250))
      pygame.draw.rect(screen,(0,0,0),Rect(10,50,300,600),5)
      pygame.draw.rect(screen,(0,0,0),Rect(330,50,70,230),5)
      font=pygame.font.Font(None,50)
      tokuten=font.render(str(counttotal2),False,(0,0,0))
      screen.blit(tokuten,(155,660))
      hyouji(haichi,screen)
      hyouji2(nexnex,screen)
      ojamahyouji(0,ojama,screen)
      pygame.display.update()
      haichi[puyo1[2]][puyo1[1]]=0
      haichi[puyo2[2]][puyo2[1]]=0
      rakkacount=0
      '''
      pygame.event.pump()
      pressed_key=pygame.key.get_pressed()
      if pressed_key[K_LEFT]:
        idou=idouhantei(haichi2,puyo1,puyo2,1)
        if idou==1:
          puyo1[1]-=1
          puyo2[1]-=1
      if pressed_key[K_RIGHT]:
        idou=idouhantei(haichi2,puyo1,puyo2,2)
        if idou==1:
          puyo1[1]+=1
          puyo2[1]+=1
      '''
      for event in pygame.event.get():
        if event.type==QUIT:
          pygame.quit()
          sys.exit()
        if event.type==KEYDOWN:
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
            sokurakka(haichi,13,nexnex,ojama,counttotal,screen)
            soku+=1
            if haichi[11][2]!=0:
              pygame.quit()
              sys.exit()
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
      pygame.event.clear()
      if soku!=0:
        break
      if soku2!=0:
        continue
      time.sleep(1)
      idou=idouhantei(haichi2,puyo1,puyo2,3)
      if idou==1:
        puyo1[2]-=1
        puyo2[2]-=1
        rakkacount+=1
      haichi[puyo1[2]][puyo1[1]]=puyo1[0]
      haichi[puyo2[2]][puyo2[1]]=puyo2[0]
      if haichi[11][2]!=0 and rakkacount==0:
        pygame.quit()
        sys.exit()
      if rakkacount==0:
        rakkacount=rakka(haichi,13,nexnex,ojama,counttotal,screen)
        break 
    rensa(haichi,nexnex,ojama,0,screen)
    screen.fill((250,250,250))
    pygame.draw.rect(screen,(0,0,0),Rect(10,50,300,600),5)
    pygame.draw.rect(screen,(0,0,0),Rect(330,50,70,230),5)
    font=pygame.font.Font(None,50)
    tokuten=font.render(str(counttotal2),False,(0,0,0))
    screen.blit(tokuten,(155,660))
    hyouji(haichi,screen)
    hyouji2(nexnex,screen)
    ojamahyouji(counttotal,ojama,screen)
    pygame.display.update()
#    print(counttotal)
    counttotal=0
#    print (counttotal2)
    for event in pygame.event.get():
      if event.type==QUIT:
        pygame.quit()
        sys.exit()
if __name__=="__main__":
  main()
