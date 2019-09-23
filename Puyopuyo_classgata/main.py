import pygame
from pygame.locals import *
import threading
import time
import sys
import random

#----self module----
from puyoclass import Puyo
from fieldclass import Field
from tumoclass import Tumo
from aiclass import AI
from elseclass import *
from hyouji import *


def main():
  gamen.start()
  while True:
    start_c=0
    for event in pygame.event.get():
      if event.type==QUIT:
        pygame.quit()
        sys.exit()
      if event.type==KEYDOWN:
        if event.key==K_a:
          start_c=1
          break
        if event.key==K_b:
          start_c=2
          break
        if event.key==K_c:
          start_c=3
        if event.key==K_d:
          start_c=4
    if start_c!=0:
      break
  if start_c==1:
    player1.start()
    karaplayer.start()
  if start_c==2:
    player1.start()
    cpu.start()
  if start_c==3:
    player1.start()
    player2.start()
  if start_c==4:
    cpu.start()
    cpu2.start()


class Gamen(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
  def run(self):
    while (1):
      if syuuryou.syuuryou_c==0:
        pygame.quit()
        sys.exit()
      allhyouji(field1,field2,puyo_1,puyo_2,screen,font)

class Player1(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
  def run (self):
    clock=pygame.time.Clock()
    puyo_1.syote(tumo)
    time.sleep(2)
    while True:
      pygame.event.pump()
      field1.haichi_c=1
      puyo_1.syokika(tumo)
      souevent.tuika()
      souevent.sakujo(K_u,K_i)
      while True:
        if syuuryou.syuuryou_c==0:
          pygame.quit()
          sys.exit()
        clock.tick(60)
        puyo_1.surinukecount+=1
        puyo_1.surinukecount2+=1
        puyo_1.yokoidou(field1)
        pressed_key=pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
          puyo_1.hidari_c+=1
        if pressed_key[K_RIGHT]:
          puyo_1.migi_c+=1
        if pressed_key[K_DOWN]:
          idou=puyo_1.idouhantei(field1,3)
          if idou==1:
            puyo_1.idou_c+=10
            puyo_1.rakkab_c+=1
          elif idou==0:
            puyo_1.setticount+=20
        souevent.tuika()
        for event in souevent.souevent:
          if event.type==QUIT:
            syuuryou.syuuryou_c=0
            pygame.quit()
            sys.exit()
          if event.type==KEYDOWN:
            if event.key==K_a:
              puyo_1.hidarikaiten(field1)
            if event.key==K_f:
              puyo_1.migikaiten(field1)
        souevent.sakujo(K_u,K_i)
        break_c=puyo_1.shitaidou(field1)
        if break_c==1:
          break
      pygame.event.pump()
      time.sleep(0.4)
      countcheck=field1.counttotal2
      field1.rensa(field2)
      field1.counttotal_a+=field1.counttotal
      field1.counttotal=0
      field1.rensa_c=0
      if countcheck!=field1.counttotal2:
        field1.zenkeshicount=0
        for i in range(1,14):
          for j in range(1,7):
            if field1.haichi[i][j]!=0:
              field1.zenkeshicount+=1
        if field1.zenkeshicount==0:
          field1.zenkeshihyouji=1
      if field2.counttotal_a>=70:
        field2.counttotal_a=field1.ojamarakka(field2)
      if field1.haichi[12][3]!=0 :
        syuuryou.syuuryou_c=0
        pygame.quit()
        sys.exit()

class Player2(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
  def run (self):
    clock=pygame.time.Clock()
    puyo_2.syote(tumo)
    time.sleep(2)
    while True:
      field2.haichi_c=1
      puyo_2.syokika2(tumo)
      while True:
        if syuuryou.syuuryou_c==0:
          pygame.quit()
          sys.exit()
        clock.tick(60)
        puyo_2.surinukecount+=1
        puyo_2.surinukecount2+=1
        puyo_2.yokoidou(field2)
        pygame.event.pump()
        pressed_key=pygame.key.get_pressed()
        if pressed_key[K_h]:
          puyo_2.hidari_c+=1
        if pressed_key[K_k]:
          puyo_2.migi_c+=1
        if pressed_key[K_j]:
          idou=puyo_2.idouhantei(field2,3)
          if idou==1:
            puyo_2.idou_c+=10
            puyo_2.rakkab_c+=1
          elif idou==0:
            puyo_2.setticount+=50
        souevent.tuika()
        for event in souevent.souevent:
          if event.type==QUIT:
            syuuryou.syuuryou_c=0
            pygame.quit()
            sys.exit()
          if event.type==KEYDOWN:
            if event.key==K_u:
              puyo_2.hidarikaiten(field2)
            if event.key==K_i:
              puyo_2.migikaiten(field2)
        souevent.sakujo(K_a,K_f)
        break_c=puyo_2.shitaidou(field2)
        if break_c==1:
          break
      time.sleep(0.4)
      countcheck=field2.counttotal2
      field2.rensa(field1)
      field2.counttotal_a+=field2.counttotal
      field2.counttotal=0
      field2.rensa_c=0
      if countcheck!=field2.counttotal2:
        field2.zenkeshicount=0
        for i in range(1,14):
          for j in range(1,7):
            if field2.haichi[i][j]!=0:
              field2.zenkeshicount+=1
        if field2.zenkeshicount==0:
          field2.zenkeshihyouji=1
      if field1.counttotal_a>=70:
        field1.counttotal_a=field2.ojamarakka(field1)
      if field2.haichi[12][3]!=0 :
        syuuryou.syuuryou_c=0
        pygame.quit()
        sys.exit()

class CPU(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
  def run (self):
    clock=pygame.time.Clock()
    puyo_2.syote(tumo)
    time.sleep(2)
    t_total=0
    t_kaisuu=0
    while True:
      t_kaisuu+=1
      field2.haichi_c=1
      puyo_2.syokika2(tumo)
      t1=time.time()
#     ai.cpu_c=ai.cpu1(field2,puyo_2)
#     ai.cpu_c=ai.cpu2(field2,puyo_2)
#     ai.cpu_c=ai.cpu3(field2,puyo_2)
      ai.cpu_c=ai.cpu4(field2,puyo_2)
      t2=time.time()
      if t_kaisuu!=1:
        t_total+=t2-t1
        print(t_total/t_kaisuu)
      while True:
        if syuuryou.syuuryou_c==0:
          pygame.quit()
          sys.exit()
        clock.tick(60)
        puyo_2.surinukecount+=1
        puyo_2.surinukecount2+=1
        puyo_2.kaiten_c=0
        ai.cpu_sousa(field2,puyo_2)
        puyo_2.yokoidou(field2)
        if puyo_2.shita_c>0:
          idou=puyo_2.idouhantei(field2,3)
          if idou==1:
            puyo_2.idou_c+=10
            puyo_2.rakkab_c+=1
          elif idou==0:
            puyo_2.setticount+=50
        if puyo_2.kaiten_c==1:
          puyo_2.hidarikaiten(field2)
        elif puyo_2.kaiten_c==2:
          puyo_2.migikaiten(field2)
        break_c=puyo_2.shitaidou(field2)
        if break_c==1:
          break
      time.sleep(0.4)
      countcheck=field2.counttotal2
      field2.rensa(field1)
      field2.counttotal_a+=field2.counttotal
      field2.counttotal=0
      field2.rensa_c=0
      if countcheck!=field2.counttotal2:
        field2.zenkeshicount=0
        for i in range(1,14):
          for j in range(1,7):
            if field2.haichi[i][j]!=0:
              field2.zenkeshicount+=1
        if field2.zenkeshicount==0:
          field2.zenkeshihyouji=1
      if field1.counttotal_a>=70:
        field1.counttotal_a=field2.ojamarakka(field1)
      if field2.haichi[12][3]!=0 :
        syuuryou.syuuryou_c=0
        pygame.quit()
        sys.exit()

class CPU2(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
  def run (self):
    clock=pygame.time.Clock()
    puyo_1.syote(tumo)
    time.sleep(2)
    t_total=0
    t_kaisuu=0
    while True:
      t_kaisuu+=1
      field1.haichi_c=1
      puyo_1.syokika(tumo)
      t1=time.time()
#     ai.cpu_c=ai.cpu1(field2,puyo_2)
#     ai.cpu_c=ai.cpu2(field2,puyo_2)
      ai2.cpu_c=ai2.cpu3(field1,puyo_1)
#     ai.cpu_c=ai.cpu4(field2,puyo_2)
      t2=time.time()
      if t_kaisuu!=1:
        t_total+=t2-t1
        print(t_total/t_kaisuu)
      while True:
        if syuuryou.syuuryou_c==0:
          pygame.quit()
          sys.exit()
        clock.tick(60)
        puyo_1.surinukecount+=1
        puyo_1.surinukecount2+=1
        puyo_1.kaiten_c=0
        ai2.cpu_sousa(field1,puyo_1)
        puyo_1.yokoidou(field1)
        if puyo_1.shita_c>0:
          idou=puyo_1.idouhantei(field1,3)
          if idou==1:
            puyo_1.idou_c+=10
            puyo_1.rakkab_c+=1
          elif idou==0:
            puyo_1.setticount+=50
        if puyo_1.kaiten_c==1:
          puyo_1.hidarikaiten(field1)
        elif puyo_1.kaiten_c==2:
          puyo_1.migikaiten(field1)
        break_c=puyo_1.shitaidou(field1)
        if break_c==1:
          break
      time.sleep(0.4)
      countcheck=field1.counttotal2
      field1.rensa(field2)
      field1.counttotal_a+=field1.counttotal
      field1.counttotal=0
      field1.rensa_c=0
      if countcheck!=field1.counttotal2:
        field1.zenkeshicount=0
        for i in range(1,14):
          for j in range(1,7):
            if field1.haichi[i][j]!=0:
              field1.zenkeshicount+=1
        if field1.zenkeshicount==0:
          field1.zenkeshihyouji=1
      if field2.counttotal_a>=70:
        field2.counttotal_a=field1.ojamarakka(field2)
      if field1.haichi[12][3]!=0 :
        syuuryou.syuuryou_c=0
        pygame.quit()
        sys.exit()


class Karaplayer(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    return

  def run (self):
    time.sleep(2)
    while True:
      if syuuryou.syuuryou_c==0:
        pygame.quit()
        sys.exit()
      if field1.counttotal_a>=70:
        field1.counttotal_a=field2.ojamarakka(field1)

if __name__=='__main__':
  #object
  syuuryou=Syuuryou()
  tumo=Tumo()
  field1=Field()
  field2=Field()
  puyo_1=Puyo(tumo)
  puyo_2=Puyo(tumo)
  ai=AI()
  ai2=AI()
  souevent=Event()
  
  #player
  player1=Player1()
  cpu=CPU()
  cpu2=CPU2()
  player2=Player2()
  karaplayer=Karaplayer()
  
  #hyouji
  gamen=Gamen()
  
  #pygame
  pygame.init()
  screen=pygame.display.set_mode((860,700))
  pygame.display.set_caption("taisen")
  font=pygame.font.Font(None,50)
 
  #start
  main()

