import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as figure
import pylab
import matplotlib.patches as patches
import time
import copy
pylab.figure(figsize=(6,12))
ax=plt.gca()
plt.xlim(xmin=0)
plt.xlim(xmax=6)
plt.ylim(ymin=0)
plt.ylim(ymax=12)
counttotal=0
def hyouji(x):
  pylab.figure(figsize=(6,12))
  ax=plt.gca()
  plt.xlim(xmin=0)
  plt.xlim(xmax=6)
  plt.ylim(ymin=0)
  plt.ylim(ymax=12)
  for j in range(12):
    for i in range(6):
      if x[j][i]==1:
        c=patches.Circle(xy=(i+0.5,j+0.5),radius=0.5,fc='b',ec='b')
        ax.add_patch(c)
      elif x[j][i]==2:
        c=patches.Circle(xy=(i+0.5,j+0.5),radius=0.5,fc='g',ec='g')
        ax.add_patch(c)
      elif x[j][i]==3:
        c=patches.Circle(xy=(i+0.5,j+0.5),radius=0.5,fc='r',ec='r')
        ax.add_patch(c)
      elif x[j][i]==4:
        c=patches.Circle(xy=(i+0.5,j+0.5),radius=0.5,fc='y',ec='y')
        ax.add_patch(c)

def rakka(x):
  count2=0
  while True:
    count=0
    for j in range(1,13):
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
def renketu(x,i,j):
  a=x[j][i]
  if a==0 or a==11 or a==12 or a==13 or a==14:
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
  if i!=0:
    if a==x[j][i-1] :
      renketu(x,i-1,j)
  if j!=11:
    if a==x[j+1][i]:
      renketu(x,i,j+1)
  if j!=0:
    if a==x[j-1][i]:
      renketu(x,i,j-1)
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
            if x[l][k]==11 or x[l][k]==12 or x[l][k]==13 or x[l][k]==14:
              x[l][k]=0
      else:
        for l in range(12):
          for k in range(6):
            if x[l][k]==11 or x[l][k]==12 or x[l][k]==13 or x[l][k]==14:
              x[l][k]=y[l][k]
  count6=irosuu[0]+irosuu[1]+irosuu[2]+irosuu[3]
  return count3,count4,count6
def rensa(x,i):
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
  if k==0:
    k=1
  counttotal+=j[0]*k*10
  hyouji(x)
  plt.savefig('/home/harada/python2/result_puyo.png')
  time.sleep(1)
  plt.close()
  y=rakka(x)
  if y==1:
    return 1
  i+=1
  rensa(x,i)


