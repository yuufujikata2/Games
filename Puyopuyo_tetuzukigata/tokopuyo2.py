import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as figure
import pylab
import matplotlib.patches as patches
import time
import copy
import pickle
import random
import sys
import pygame
from pygame.locals import *

class Puyo:
  def __init__(self,a,b):
    self.num1=a
    self.num2=b
  def rakka(self,map):
    for j in range(1,y):
      for i in range(6):
        if x[j][i]!=0 and x[j-1][i]==0:
          x[j-1][i]=x[j][i]
          x[j][i]=0


class Map:
  row,col=13,8
  map=[[6,0,0,0,0,0,0,6],
       [6,0,0,0,0,0,0,6],
       [6,0,0,0,0,0,0,6],
       [6,0,0,0,0,0,0,6],
       [6,0,0,0,0,0,0,6],
       [6,0,0,0,0,0,0,6],
       [6,0,0,0,0,0,0,6],
       [6,0,0,0,0,0,0,6],
       [6,0,0,0,0,0,0,6],
       [6,0,0,0,0,0,0,6],
       [6,0,0,0,0,0,0,6],
       [6,0,0,0,0,0,0,6],
       [6,0,0,0,0,0,0,6]]
  
  def hyouji(self,screen):
    screen.fill((250,250,250))
    for i in range(12):
      for j in range(6):
        if map[i][j]==1:
          s=50*(11.5-i)
          s=int(s)
          k=j+0.5
          k=int(50*k)
          pygame.draw.circle(screen,(250,0,0),(k,s),25)
        elif map[i][j]==2:
          s=50*(11.5-i)
          s=int(s)
          k=j+0.5
          k=int(50*k)
          pygame.draw.circle(screen,(0,250,0),(k,s),25)
        elif map[i][j]==3:
          s=50*(11.5-i)
          s=int(s)
          k=j+0.5
          k=int(50*k)
          pygame.draw.circle(screen,(0,0,250),(k,s),25)
        elif map[i][j]==4:
          s=50*(11.5-i)
          s=int(s)
          k=j+0.5
          k=int(50*k)
          pygame.draw.circle(screen,(250,250,0),(k,s),25)
    pygame.display.update()















def ojamahyouji(x,y):
    y[0]=0
    y[1]=0
    y[2]=0
    y[3]=0
    y[4]=0
    y[5]=0
    x=x/70
    hoshi=x/180
    iwa=(x % 180)/30
    oo=(x % 30)/6
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
    hyouji3(y)
    plt.savefig('/home/harada/python2/result_puyo3.png')
    plt.close

def rakka(x,y):
  count2=0
  while True:
    count=0
    for j in range(1,y):
      for i in range(6):
        if x[j][i]!=0 and x[j-1][i]==0:
          count+=1
          x[j-1][i]=x[j][i]
          x[j][i]=0
    hyouji(x)
    plt.savefig('/home/harada/python2/result_puyo.png')
    time.sleep(1)
    plt.close()
    count2+=1
    if count==0:
      break
  return count2
def sokurakka(x,y):
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
    if count==0:
      break
  hyouji(x)
  plt.savefig('/home/harada/python2/result_puyo.png')
  plt.close()
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
def rensa(x,i):
  i+=1
  global counttotal
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
  hyouji(x)
  plt.savefig('/home/harada/python2/result_puyo.png')
  time.sleep(1)
  plt.close()
  y=rakka(x,13)
  if y==1:
    return 1
  rensa(x,i)
def ojamarakka(x,y,z,nexnex,n1,n2,n3,n4,n5,n6):
  global counttotal2
  while y>2100:
    x.append([0,0,0,0,0,0])
    x.append([0,0,0,0,0,0])
    x.append([0,0,0,0,0,0])
    x.append([0,0,0,0,0,0])
    x.append([0,0,0,0,0,0])
    y-=2100
    ojamahyouji(y,z)
    for j in range(13,18):
      for i in range(6):
        x[j][i]=5
    rakka(x,18)
    x.pop(17)
    x.pop(16)
    x.pop(15)
    x.pop(14)
    x.pop(13)
    s=copy.deepcopy(x)
    x.append([0,0,0,0,0,0])
    x.append([0,0,0,0,0,0])
    n7=random.randint(1,4)
    n8=random.randint(1,4)
    nexnex[0]=n6
    nexnex[1]=n5
    nexnex[3]=n4
    nexnex[4]=n3
    nexnex[6]=n2
    nexnex[7]=n1
    hyouji2(nexnex)
    plt.savefig('/home/harada/python2/result_puyo2.png')
    plt.close
    print(n1)
    print(n2)
    print('next')
    print(n3)
    print(n4)
    print('nextnext')
    print(n5)
    print(n6)
    r=raw_input()
    if r=='hh':
      x[14][0]=n1
      x[13][0]=n2
    elif r=='hhaa':
      x[14][0]=n2
      x[13][0]=n1
    elif r=='h':
      x[14][1]=n1
      x[13][1]=n2
    elif r=='haa':
      x[14][1]=n2
      x[13][1]=n1
    elif r=='d':
      x[14][2]=n1
      x[13][2]=n2
    elif r=='aa':
      x[14][2]=n2
      x[13][2]=n1
    elif r=='l':
      x[14][3]=n1
      x[13][3]=n2
    elif r=='laa':
      x[14][3]=n2
      x[13][3]=n1
    elif r=='ll':
      x[14][4]=n1
      x[13][4]=n2
    elif r=='llaa':
      x[14][4]=n2
      x[13][4]=n1
    elif r=='lll':
      x[14][5]=n1
      x[13][5]=n2
    elif r=='lllaa':
      x[14][5]=n2
      x[13][5]=n1
    elif r=='ha':
      x[13][0]=n1
      x[13][1]=n2
    elif r=='a':
      x[13][1]=n1
      x[13][2]=n2
    elif r=='la':
      x[13][2]=n1
      x[13][3]=n2
    elif r=='lla':
      x[13][3]=n1
      x[13][4]=n2
    elif r=='llla':
      x[13][4]=n1
      x[13][5]=n2
    elif r=='hhb':
      x[13][0]=n2
      x[13][1]=n1
    elif r=='hb':
      x[13][1]=n2
      x[13][2]=n1
    elif r=='b':
      x[13][2]=n2
      x[13][3]=n1
    elif r=='lb':
      x[13][3]=n2
      x[13][4]=n1
    elif r=='llb':
      x[13][4]=n2
      x[13][5]=n1
    plt.close()
    n01=n1
    n02=n2
    n1=n3
    n2=n4
    n3=n5
    n4=n6
    n5=n7
    n6=n8
    rakka(x,15)
    x.pop(14)
    x.pop(13)
    hyouji(x)
    rensa(x,0)
    hyouji(x)
    f=open('haichifile.binaryfile','wb')
    pickle.dump(x,f)
    f.close
    counttotal2+=counttotal
    print(counttotal2)
    if x[11][2]!=0:
      sys.exit()
  ojamahyouji(y,z)
  time.sleep(1)
  x.append([0,0,0,0,0,0])
  x.append([0,0,0,0,0,0])
  x.append([0,0,0,0,0,0])
  x.append([0,0,0,0,0,0])
  x.append([0,0,0,0,0,0])
  y1=y/70
  if y1>24:
    for j in range(13,17):
      for i in range(6):
        x[j][i]=5
    o=random.sample(range(6),6)
    for i in range(y1-24):
      x[17][o[i]]=5
  elif y1>18:
    for j in range(13,16):
      for i in range(6):
        x[j][i]=5
    o=random.sample(range(6),6)
    for i in range(y1-18):
      x[16][o[i]]=5
  elif y1>12:
    for j in range(13,15):
      for i in range(6):
        x[j][i]=5
    o=random.sample(range(6),6)
    for i in range(y1-12):
      x[15][o[i]]=5
  elif y1>6:
    for j in range(13,14):
      for i in range(6):
        x[j][i]=5
    o=random.sample(range(6),6)
    for i in range(y1-6):
      x[14][o[i]]=5
  else:
    o=random.sample(range(6),6)
    for i in range(y1):
      x[13][o[i]]=5
  ojamahyouji(0,z)
  rakka(x,18)
  x.pop(17)
  x.pop(16)
  x.pop(15)
  x.pop(14)
  x.pop(13)
  return n01,n02,n1,n2,n3,n4,n5,n6






nexnex=[0,0,0,0,0,0,0,0]
ojama=[0,0,0,0,0,0]
counttotal2=0
print('do you want to delete haichi?')
delete=raw_input()
if delete=='y':
  haichi=[[0 for i in range(6)] for j in range(13)]
  f=open('haichifile.binaryfile','wb')
  pickle.dump(haichi,f)
  f.close
  n1=random.randint(1,3)
  n2=random.randint(1,3)
  n3=random.randint(1,3)
  n4=random.randint(1,3)
  n5=random.randint(1,4)
  n6=random.randint(1,4)
  nexnex[0]=n6
  nexnex[1]=n5
  nexnex[3]=n4
  nexnex[4]=n3
  nexnex[6]=n2
  nexnex[7]=n1
  g=open('nexnexfile.binaryfile','wb')
  pickle.dump(nexnex,g)
  g.close

with open('haichifile.binaryfile','rb') as f:
  haichi=pickle.load(f)
  hyouji(haichi)
  plt.savefig('/home/harada/python2/result_puyo.png')
with open('nexnexfile.binaryfile','rb') as g:
  nexnex=pickle.load(g)
  hyouji2(nexnex)
  plt.savefig('/home/harada/python2/result_puyo2.png')
n6=nexnex[0]
n5=nexnex[1]
n4=nexnex[3]
n3=nexnex[4]
n2=nexnex[6]
n1=nexnex[7]
while True:
  if haichi[11][2]!=0:
    break
  counttotal=0
  with open('haichifile.binaryfile','rb') as f:
    haichi=pickle.load(f)
    hyouji(haichi)
    plt.savefig('/home/harada/python2/result_puyo.png')
  print('continue?')
  n=raw_input()
  if n=='y':
    s=copy.deepcopy(haichi)
    haichi.append([0,0,0,0,0,0])
    haichi.append([0,0,0,0,0,0])
    n7=random.randint(1,4)
    n8=random.randint(1,4)
    nexnex[0]=n6
    nexnex[1]=n5
    nexnex[3]=n4
    nexnex[4]=n3
    nexnex[6]=n2
    nexnex[7]=n1
    hyouji2(nexnex)
    plt.savefig('/home/harada/python2/result_puyo2.png')
    plt.close
    print(n1)
    print(n2)
    print('next')
    print(n3)
    print(n4)
    print('nextnext')
    print(n5)
    print(n6)
    r=raw_input()
    nexnex[0]=n8
    nexnex[1]=n7
    nexnex[3]=n6
    nexnex[4]=n5
    nexnex[6]=n4
    nexnex[7]=n3
    hyouji2(nexnex)
    plt.savefig('/home/harada/python2/result_puyo2.png')
    plt.close
    if r=='hh':
      haichi[14][0]=n1
      haichi[13][0]=n2
    elif r=='hhaa':
      haichi[14][0]=n2
      haichi[13][0]=n1
    elif r=='h':
      haichi[14][1]=n1
      haichi[13][1]=n2
    elif r=='haa':
      haichi[14][1]=n2
      haichi[13][1]=n1
    elif r=='d':
      haichi[14][2]=n1
      haichi[13][2]=n2
    elif r=='aa':
      haichi[14][2]=n2
      haichi[13][2]=n1
    elif r=='l':
      haichi[14][3]=n1
      haichi[13][3]=n2
    elif r=='laa':
      haichi[14][3]=n2
      haichi[13][3]=n1
    elif r=='ll':
      haichi[14][4]=n1
      haichi[13][4]=n2
    elif r=='llaa':
      haichi[14][4]=n2
      haichi[13][4]=n1
    elif r=='lll':
      haichi[14][5]=n1
      haichi[13][5]=n2
    elif r=='lllaa':
      haichi[14][5]=n2
      haichi[13][5]=n1
    elif r=='ha':
      haichi[13][0]=n1
      haichi[13][1]=n2
    elif r=='a':
      haichi[13][1]=n1
      haichi[13][2]=n2
    elif r=='la':
      haichi[13][2]=n1
      haichi[13][3]=n2
    elif r=='lla':
      haichi[13][3]=n1
      haichi[13][4]=n2
    elif r=='llla':
      haichi[13][4]=n1
      haichi[13][5]=n2
    elif r=='hhb':
      haichi[13][0]=n2
      haichi[13][1]=n1
    elif r=='hb':
      haichi[13][1]=n2
      haichi[13][2]=n1
    elif r=='b':
      haichi[13][2]=n2
      haichi[13][3]=n1
    elif r=='lb':
      haichi[13][3]=n2
      haichi[13][4]=n1
    elif r=='llb':
      haichi[13][4]=n2
      haichi[13][5]=n1
    plt.close()
    rakka(haichi,15)
    haichi.pop(14)
    haichi.pop(13)
    hyouji(haichi)
    rensa(haichi,0)
    hyouji(haichi)
    f=open('haichifile.binaryfile','wb')
    pickle.dump(haichi,f)
    f.close
    counttotal2+=counttotal
    print('point')
    print(counttotal)
    print('pointtotal')
    print(counttotal2)
    n01=n1
    n02=n2
    n1=n3
    n2=n4
    n3=n5
    n4=n6
    n5=n7
    n6=n8
  elif n=='r':
    print('return')
    haichi=copy.deepcopy(s)
    hyouji(haichi)
    f=open('haichifile.binaryfile','wb')
    pickle.dump(haichi,f)
    f.close
    plt.savefig('/home/harada/python2/result_puyo.png')
    plt.close
    n8=n6
    n7=n5
    n6=n4
    n5=n3
    n4=n2
    n3=n1
    n2=n02
    n1=n01
  elif n=='o':
    ojama=[0,0,0,0,0,0]
    print('ojama')
    o_count=int(raw_input())
    ojamahyouji(o_count,ojama)
    time.sleep(1)
    ni=ojamarakka(haichi,o_count,ojama,nexnex,n1,n2,n3,n4,n5,n6)
    n01=ni[0]
    n02=ni[1]
    n1=ni[2]
    n2=ni[3]
    n3=ni[4]
    n4=ni[5]
    n5=ni[6]
    n6=ni[7]
    f=open('haichifile.binaryfile','wb')
    pickle.dump(haichi,f)
    f.close
  else:
    g=open('nexnexfile.binaryfile','wb')
    pickle.dump(nexnex,g)
    g.close
    break

