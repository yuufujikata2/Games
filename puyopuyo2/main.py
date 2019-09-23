import pygame
from pygame.locals import *
import threading
import time
import sys
import random
from cProfile import Profile

#----self module----
from puyoclass import Puyo
from puyoclass import AIPuyo
from fieldclass import Field
from fieldclass import AIField
from tumoclass import Tumo
from aiclass import CPU
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
    if start_c!=0:
      break
  if start_c==1:
    player1.start()
    karaplayer.start()
  if start_c==2:
    com_migi.start()
    ai_cpu3_migi.start()
    player1.start()

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
      countcheck=field1.tokuten.behind 
      field1.rensa(field2)
      field1.rensa_c=0
      if countcheck!=field1.tokuten.behind:
        field1.tokuten.atack += field1.tokuten.behind
        field1.tokuten.behind = 0
        field1.zenkeshicount=0
        for i in range(1,14):
          for j in range(1,7):
            if field1.haichi[i][j]!=0:
              field1.zenkeshicount+=1
        if field1.zenkeshicount==0:
          field1.tokuten.behind_behind += 2100
          field1.tokuten.hyouji += 2100
          field1.zenkeshihyouji=1
      if field2.tokuten.atack>=70:
        field1.ojamarakka(field2)
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


class COM(threading.Thread):
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
      tugipuyo=AIPuyo()
      tugipuyo.puyo1iro=puyo_1.nexnex[0]
      tugipuyo.puyo2iro=puyo_1.nexnex[1]
      tugipuyo.puyo1x=3
      tugipuyo.puyo1y=13
      tugipuyo.puyo2x=3
      tugipuyo.puyo2y=12 
      t1=time.time()
      cpu.cpu_c=cpu.ai5(field1.haichi,puyo_1,tugipuyo)
      t2=time.time()
      print(t2-t1)
      print(cpu.cpu_c)
#     if t_kaisuu!=1:
#       t_total+=t2-t1
#       print(t_total/t_kaisuu)
      while True:
        if syuuryou.syuuryou_c==0:
          pygame.quit()
          sys.exit()
        clock.tick(60)
        puyo_1.surinukecount+=1
        puyo_1.surinukecount2+=1
        puyo_1.kaiten_c=0
        cpu.cpu_sousa_c=cpu.cpu_sousa(field1,puyo_1)
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


class COM_MIGI(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
  def run (self):
    clock=pygame.time.Clock()
    puyo_2.syote(tumo)
    time.sleep(2)
    puyo_2.hajime_c=0
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
        puyo_2.kaiten_c=0
        if puyo_2.imapuyo_c==1:
          cpu2.cpu_sousa_c=cpu2.cpu_sousa(field2,puyo_2)
        else:
          cpu2.cpu_sousa_c=0
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
      countcheck=field2.tokuten.behind
      field2.rensa(field1)
      field2.rensa_c=0
      if countcheck!=field2.tokuten.behind:
        field2.tokuten.atack += field2.tokuten.behind
        field2.tokuten.behind = 0
        field2.zenkeshicount=0
        for i in range(1,14):
          for j in range(1,7):
            if field2.haichi[i][j]!=0:
              field2.zenkeshicount+=1
        if field2.zenkeshicount==0:
          field2.tokuten.behind_behind += 2100
          field2.tokuten.hyouji += 2100
          field2.zenkeshihyouji = 1
      if field1.tokuten.atack >= 70:
        field2.ojamarakka(field1)
      if field2.haichi[12][3]!=0 :
        syuuryou.syuuryou_c=0
        pygame.quit()
        sys.exit()



class COM_HIDARI(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
  def run (self):
    clock=pygame.time.Clock()
    puyo_1.syote(tumo)
    time.sleep(2)
    puyo_1.hajime_c=0
    while True:
      field1.haichi_c=1
      puyo_1.syokika(tumo)
      while True:
        if syuuryou.syuuryou_c==0:
          pygame.quit()
          sys.exit()
        clock.tick(60)
        puyo_1.surinukecount+=1
        puyo_1.surinukecount2+=1
        puyo_1.kaiten_c=0
        if puyo_1.imapuyo_c==1:
          cpu.cpu_sousa_c=cpu.cpu_sousa(field1,puyo_1)
        else:
          cpu.cpu_sousa_c=0
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
      time.sleep(0.5)
      if syuuryou.syuuryou_c==0:
        pygame.quit()
        sys.exit()
      if field1.tokuten.atack>=70:
        field2.ojamarakka(field1)

class AI_CPU(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    return
  def run(self):
    sakiyomicpu_c=0
    kirikae_c=0
    while True:
      if kirikae_c==0:
        karifield=AIField(field2.haichi)
        karipuyo=AIPuyo()
        karipuyo.syokika(puyo_2) 
        karipuyo.puyooki(cpu2.cpu_c)
        karipuyo.rakka(karifield.haichi)
        karifield.sokurensa()
        imapuyo=AIPuyo()
        imapuyo.puyo1iro=puyo_2.nexnex[0]
        imapuyo.puyo2iro=puyo_2.nexnex[1]
        if puyo_2.hajime_c==1:
          imapuyo.puyo1x=3
          imapuyo.puyo1y=13
          imapuyo.puyo2x=3
          imapuyo.puyo2y=12
        else:
          imapuyo.puyo1x=puyo_2.puyo1x
          imapuyo.puyo1y=puyo_2.puyo1y
          imapuyo.puyo2x=puyo_2.puyo2x
          imapuyo.puyo2y=puyo_2.puyo2y
#        t1=time.time()
        sakiyomicpu_c=cpu2.ai4(karifield.haichi,imapuyo)
#        t2=time.time()
#        print(t2-t1)
        kirikae_c=1
      else:
        if puyo_2.imapuyo_c==0:
          cpu2.cpu_c=sakiyomicpu_c
#          print(cpu2.cpu_c)
          kirikae_c=0
          puyo_2.imapuyo_c=1
        time.sleep(0.001)

class AI_CPU2(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    return
  def run(self):
    sakiyomicpu_c=0
    kirikae_c=0
    sousamati_c=0
    while True:
      if cpu2.cpu_sousa_c==0:
        sousamati_c+=1
      else:
        sousamati_c=0
      if sousamati_c>=30:
        karifield=AIField(field2.haichi)
        imapuyo=AIPuyo()
        imapuyo.syokika(puyo_2)
        imapuyo2=AIPuyo()
        imapuyo2.puyo1iro=puyo_2.nexnex[0]
        imapuyo2.puyo2iro=puyo_2.nexnex[1]
        imapuyo2.puyo1x=3
        imapuyo2.puyo1y=13
        imapuyo2.puyo2x=3
        imapuyo2.puyo2y=12
        cpu2.cpu_c=cpu2.ai7(karifield.haichi,imapuyo,imapuyo2)
        time.sleep(0.001)
        sousamati_c=0
         
      if kirikae_c==0:
        karifield=AIField(field2.haichi)
        karipuyo=AIPuyo()
        karipuyo.syokika(puyo_2) 
        karipuyo.puyooki(cpu2.cpu_c)
        karipuyo.rakka(karifield.haichi)
        karifield.sokurensa()
        imapuyo=AIPuyo()
        imapuyo2=AIPuyo()
        imapuyo.puyo1iro=puyo_2.nexnex[0]
        imapuyo.puyo2iro=puyo_2.nexnex[1]
        imapuyo2.puyo1iro=puyo_2.nexnex[2]
        imapuyo2.puyo2iro=puyo_2.nexnex[3]
        imapuyo.puyo1x=3
        imapuyo.puyo1y=13
        imapuyo.puyo2x=3
        imapuyo.puyo2y=12
        imapuyo2.puyo1x=3
        imapuyo2.puyo1y=13
        imapuyo2.puyo2x=3
        imapuyo2.puyo2y=12
#        t1=time.time()
#        pr=Profile()
#        pr.enable()
        sakiyomicpu_c=cpu2.ai7(karifield.haichi,imapuyo,imapuyo2)
#        pr.disable()
#        pr.print_stats()
#        t2=time.time()
#        print(t2-t1)
        kirikae_c=1
        sousamati_c=0
      else:
        if puyo_2.imapuyo_c==0:
          cpu2.cpu_c=sakiyomicpu_c
#          print(cpu2.cpu_c)
          kirikae_c=0
          puyo_2.imapuyo_c=1
        time.sleep(0.001)

class AI_CPU3_hidari(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    return
  def run(self):
    sakiyomicpu_c=0
    kirikae_c=0
    sousamati_c=0
    while True:
      if cpu.cpu_sousa_c==0:
        sousamati_c+=1
      else:
        sousamati_c=0
      if sousamati_c>=30:
        karifield=AIField(field1.haichi)
        karifield.zenkeshihyouji=field1.zenkeshihyouji
        imapuyo=AIPuyo()
        imapuyo.syokika(puyo_1)
        imapuyo2=AIPuyo()
        imapuyo2.puyo1iro=puyo_1.nexnex[0]
        imapuyo2.puyo2iro=puyo_1.nexnex[1]
        imapuyo2.puyo1x=3
        imapuyo2.puyo1y=13
        imapuyo2.puyo2x=3
        imapuyo2.puyo2y=12
        cpu.cpu_c=cpu.ai11(karifield,field2,imapuyo,imapuyo2)
        time.sleep(0.001)
        sousamati_c=0
         
      if kirikae_c==0:
        karifield=AIField(field1.haichi)
        karifield.zenkeshihyouji=field1.zenkeshihyouji
        karipuyo=AIPuyo()
        karipuyo.syokika(puyo_1) 
        karipuyo.puyooki(cpu.cpu_c)
        karipuyo.rakka(karifield.haichi)
        karifield.sokurensa()
        imapuyo=AIPuyo()
        imapuyo2=AIPuyo()
        imapuyo.puyo1iro=puyo_1.nexnex[0]
        imapuyo.puyo2iro=puyo_1.nexnex[1]
        imapuyo2.puyo1iro=puyo_1.nexnex[2]
        imapuyo2.puyo2iro=puyo_1.nexnex[3]
        imapuyo.puyo1x=3
        imapuyo.puyo1y=13
        imapuyo.puyo2x=3
        imapuyo.puyo2y=12
        imapuyo2.puyo1x=3
        imapuyo2.puyo1y=13
        imapuyo2.puyo2x=3
        imapuyo2.puyo2y=12
        t1=time.time()
#        pr=Profile()
#        pr.enable()
        sakiyomicpu_c=cpu.ai11(karifield,field2,imapuyo,imapuyo2)
#        pr.disable()
#        pr.print_stats()
        t2=time.time()
        print(t2-t1)
        kirikae_c=1
        sousamati_c=0
      else:
        if puyo_1.imapuyo_c==0:
          puyo_1.kaiten_c=0
          puyo_1.migi_c=0
          puyo_1.hidari_c=0
          cpu.cpu_c=sakiyomicpu_c
#          print(cpu.cpu_c)
          kirikae_c=0
          puyo_1.imapuyo_c=1
        time.sleep(0.001)

class AI_CPU3_migi(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    return
  def run(self):
    sakiyomicpu_c=0
    kirikae_c=0
    sousamati_c=0
    while True:
      if cpu.cpu_sousa_c==0:
        sousamati_c+=1
      else:
        sousamati_c=0
      if sousamati_c>=30:
        karifield=AIField(field2.haichi)
        karifield.zenkeshihyouji=field2.zenkeshihyouji
        imapuyo=AIPuyo()
        imapuyo.syokika(puyo_2)
        imapuyo2=AIPuyo()
        imapuyo2.puyo1iro=puyo_2.nexnex[0]
        imapuyo2.puyo2iro=puyo_2.nexnex[1]
        imapuyo2.puyo1x=3
        imapuyo2.puyo1y=13
        imapuyo2.puyo2x=3
        imapuyo2.puyo2y=12
        cpu2.cpu_c=cpu2.ai11(karifield,field1,imapuyo,imapuyo2)
        time.sleep(0.001)
        sousamati_c=0
         
      if kirikae_c==0:
        karifield=AIField(field2.haichi)
        karifield.zenkeshihyouji=field2.zenkeshihyouji
        karipuyo=AIPuyo()
        karipuyo.syokika(puyo_2) 
        karipuyo.puyooki(cpu2.cpu_c)
        karipuyo.rakka(karifield.haichi)
        karifield.sokurensa()
        imapuyo=AIPuyo()
        imapuyo2=AIPuyo()
        imapuyo.puyo1iro=puyo_2.nexnex[0]
        imapuyo.puyo2iro=puyo_2.nexnex[1]
        imapuyo2.puyo1iro=puyo_2.nexnex[2]
        imapuyo2.puyo2iro=puyo_2.nexnex[3]
        imapuyo.puyo1x=3
        imapuyo.puyo1y=13
        imapuyo.puyo2x=3
        imapuyo.puyo2y=12
        imapuyo2.puyo1x=3
        imapuyo2.puyo1y=13
        imapuyo2.puyo2x=3
        imapuyo2.puyo2y=12
        t1=time.time()
#        pr=Profile()
#        pr.enable()
        sakiyomicpu_c=cpu2.ai11(karifield,field1,imapuyo,imapuyo2)
#        pr.disable()
#        pr.print_stats()
        t2=time.time()
        print(t2-t1)
        kirikae_c=1
        sousamati_c=0
      else:
        if puyo_2.imapuyo_c==0:
          puyo_2.kaiten_c=0
          puyo_2.migi_c=0
          puyo_2.hidari_c=0
          cpu2.cpu_c=sakiyomicpu_c
#          print(cpu2.cpu_c)
          kirikae_c=0
          puyo_2.imapuyo_c=1
        time.sleep(0.001)


if __name__=='__main__':
  #object
  syuuryou=Syuuryou()
  tumo=Tumo()
  field1=Field()
  field2=Field()
  puyo_1=Puyo(tumo)
  puyo_2=Puyo(tumo)
  cpu=CPU()
  cpu2=CPU()
  souevent=Event()
  
  #player
  player1=Player1()
  com_migi=COM_MIGI()
  com_hidari=COM_HIDARI()
  com=COM()
  player2=Player2()
  karaplayer=Karaplayer()

  #AI
  ai_cpu=AI_CPU()
  ai_cpu2=AI_CPU2()
  ai_cpu3_migi=AI_CPU3_migi()
  ai_cpu3_hidari=AI_CPU3_hidari()
  
  #hyouji
  gamen=Gamen()
  
  #pygame
  pygame.init()
  screen=pygame.display.set_mode((860,700))
  pygame.display.set_caption("puyopuyo")
  font=pygame.font.Font(None,50)
 
  #start
  main()

