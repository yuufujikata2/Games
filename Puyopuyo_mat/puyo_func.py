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
  if a==10:
    return 1
  x[j][i]=10
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
  for j in range(12):
    for i in range(6):
      count2=0
      y=copy.deepcopy(x)
      renketu(x,i,j)
      for l in range(12):
        for k in range(6):
          if x[l][k]==10:
            count2+=1
      if count2>=4:
        for l in range(12):
          for k in range(6):
            if x[l][k]==10:
              x[l][k]=0
      else:
        for l in range(12):
          for k in range(6):
            if x[l][k]==10:
              x[l][k]=y[l][k]
def rensa(x):
  renketukeshi(x)
  hyouji(x)
  plt.savefig('/home/harada/python2/result_puyo.png')
  time.sleep(1)
  plt.close()
  y=rakka(x)
  if y==1:
    return 1
  rensa(x)


