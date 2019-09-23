import random
import pygame
import pygame.locals import *
def cpu_sousa(haichi_2,puyo1_2,puyo2_2,x):
  global hidari_c_2,migi_c_2,shita_c_2,kaiten_c_2
  shita_c_2=0
  if x==0:
    if puyo2_2[1]!=0:
      hidari_c_2+=1
    else:
      shita_c_2+=1
  if x==1:
    if puyo2_2[1]<1:
      migi_c_2+=1:
    elif puyo1_2[1]>1:
      hidari_c_2+=1:
    else:
      shita_c_2+=1:
  if x==2:
    if puyo2_2[1]<2:
      migi_c_2+=1
    elif puyo2_2[1]>2:
      hidari_c_2+=1
    else:
      shita_c_2+=1
  if x==3:
    if puyo2_2[1]<3:
      migi_c_2+=1
    elif puyo2_2[1]>3:
      hidari_c_2+=1
    else:
      shita_c_2+=1
  if x==4:
    if puyo2_2[1]<4:
      migi_c_2+=1
    elif puyo2_2[1]>4:
      hidari_c_2+=1
    else:
      shita_c_2+=1
  if x==5:
    if puyo2_2[1]<5:
      migi_c_2+=1
    elif puyo2_2[1]>5:
      hidari_c_2+=1
    else:
      shita_c_2+=1
  if x==6:
    if haichi_2[11][1]==0 and haichi_2[11][3]==0:
      if puyo1_2[2]!=puyo2_2[2]+1:
        kaiten_c_2=1
      else:
        kaiten_c_2=0
    if puyo2_2[1]>0:
      hidari_c_2+=1
    else:
      shita_c_2+=1
  if x==7:
    if haichi_2[11][1]==0 and haichi_2[11][3]==0:
      if puyo1_2[2]!=puyo2_2[2]+1:
        kaiten_c_2=1
      else:
        kaiten_c_2=0
    if puyo2_2[1]>1:
      hidari_c_2+=1
    elif puyo2_2[1]<1:
      migi_c_2+=1
    else:
      shita_c_2+=1
  if x==8:
    if haichi_2[11][1]==0 and haichi_2[11][3]==0:
      if puyo1_2[2]!=puyo2_2[2]+1:
        kaiten_c_2=1
      else:
        kaiten_c_2=0
    if puyo2_2[1]>2:
      hidari_c_2+=1
    elif puyo2_2[1]<2:
      migi_c_2+=1
    else:
      shita_c_2+=1
  if x==9:
    if haichi_2[11][1]==0 and haichi_2[11][3]==0:
      if puyo1_2[2]!=puyo2_2[2]+1:
        kaiten_c_2=2
      else:
        kaiten_c_2=0
    if puyo2_2[1]>3:
      hidari_c_2+=1
    elif puyo2_2[1]<3:
      migi_c_2+=1
    else:
      shita_c_2+=1
  if x==10:
    if haichi_2[11][1]==0 and haichi_2[11][3]==0:
      if puyo1_2[2]!=puyo2_2[2]+1:
        kaiten_c_2=2
      else:
        kaiten_c_2=0
    if puyo2_2[1]>4:
      hidari_c_2+=1
    elif puyo2_2[1]<4:
      migi_c_2+=1
    else:
      shita_c_2+=1
  if x==11:
    if haichi_2[11][1]==0 and haichi_2[11][3]==0:
      if puyo1_2[2]!=puyo2_2[2]+1:
        kaiten_c_2=2
      else:
        kaiten_c_2=0
    if puyo2_2[1]>5:
      hidari_c_2+=1
    elif puyo2_2[1]<5:
      migi_c_2+=1
    else:
      shita_c_2+=1
  if x==12:
    if haichi_2[11][1]==0 and haichi_2[11][3]==0:
      if puyo1_2[1]!=puyo2_2[1]-1:
        kaiten_c_2=2
      else:
        kaiten_c_2=0
    if puyo2_2[1]>1:
      hidari_c_2+=1
    elif puyo2_2[1]<1:
      migi_c_2+=1
    else:
      shita_c_2+=1
  if x==13:
    if haichi_2[11][1]==0 and haichi_2[11][3]==0:
      if puyo1_2[1]!=puyo2_2[1]-1:
        kaiten_c_2=2
      else:
        kaiten_c_2=0
    if puyo2_2[1]>2:
      hidari_c_2+=1
    elif puyo2_2[1]<2:
      migi_c_2+=1
    else:
      shita_c_2+=1
  if x==14:
    if haichi_2[11][1]==0 and haichi_2[11][3]==0:
      if puyo1_2[1]!=puyo2_2[1]-1:
        kaiten_c_2=2
      else:
        kaiten_c_2=0
    if puyo2_2[1]>3:
      hidari_c_2+=1
    elif puyo2_2[1]<3:
      migi_c_2+=1
    else:
      shita_c_2+=1
  if x==15:
    if haichi_2[11][1]==0 and haichi_2[11][3]==0:
      if puyo1_2[1]!=puyo2_2[1]-1:
        kaiten_c_2=2
      else:
        kaiten_c_2=0
    if puyo2_2[1]>4:
      hidari_c_2+=1
    elif puyo2_2[1]<4:
      migi_c_2+=1
    else:
      shita_c_2+=1
  if x==16:
    if haichi_2[11][1]==0 and haichi_2[11][3]==0:
      if puyo1_2[1]!=puyo2_2[1]-1:
        kaiten_c_2=2
      else:
        kaiten_c_2=0
    if puyo2_2[1]>5:
      hidari_c_2+=1
    elif puyo2_2[1]<5:
      migi_c_2+=1
    else:
      shita_c_2+=1
  if x==17:
    if haichi_2[11][1]==0 and haichi_2[11][3]==0:
      if puyo1_2[1]!=puyo2_2[1]+1:
        kaiten_c_2=1
      else:
        kaiten_c_2=0
    if puyo2_2[1]>0:
      hidari_c_2+=1
    elif puyo2_2[1]<0:
      migi_c_2+=1
    else:
      shita_c_2+=1
  if x==18:
    if haichi_2[11][1]==0 and haichi_2[11][3]==0:
      if puyo1_2[1]!=puyo2_2[1]+1:
        kaiten_c_2=1
      else:
        kaiten_c_2=0
    if puyo2_2[1]>1:
      hidari_c_2+=1
    elif puyo2_2[1]<1:
      migi_c_2+=1
    else:
      shita_c_2+=1
  if x==19:
    if haichi_2[11][1]==0 and haichi_2[11][3]==0:
      if puyo1_2[1]!=puyo2_2[1]+1:
        kaiten_c_2=1
      else:
        kaiten_c_2=0
    if puyo2_2[1]>2:
      hidari_c_2+=1
    elif puyo2_2[1]<2:
      migi_c_2+=1
    else:
      shita_c_2+=1
  if x==20:
    if haichi_2[11][1]==0 and haichi_2[11][3]==0:
      if puyo1_2[1]!=puyo2_2[1]+1:
        kaiten_c_2=1
      else:
        kaiten_c_2=0
    if puyo2_2[1]>3:
      hidari_c_2+=1
    elif puyo2_2[1]<3:
      migi_c_2+=1
    else:
      shita_c_2+=1
  if x==21:
    if haichi_2[11][1]==0 and haichi_2[11][3]==0:
      if puyo1_2[1]!=puyo2_2[1]+1:
        kaiten_c_2=1
      else:
        kaiten_c_2=0
    if puyo2_2[1]>4:
      hidari_c_2+=1
    elif puyo2_2[1]<4:
      migi_c_2+=1
    else:
      shita_c_2+=1
  return 0      






def cpu1(haichi_2,puyo1_2,puyo2_2):
  return random.randint(0,21)
def cpu2(haichi_2,puyo1_2,puyo2_2):
  
