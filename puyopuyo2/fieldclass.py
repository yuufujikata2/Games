import time
import jisakucopy
import random
import numpy as np
from tokutenclass import Tokuten

class Field():
  def __init__(self):
    self.haichi=[[0 for i in range(8)] for j in range(15)]
    for i in range(15):
      self.haichi[i][0]=20
      self.haichi[i][7]=20
    for i in range(1,7):
      self.haichi[0][i]=20
    self.ojama=[0,0,0,0,0,0]
    self.tokuten = Tokuten()
    self.zenkeshihyouji=0
    self.rensa_c=0
    self.haichi_c=0
    self.count21=0
    self.count22=0
    self.count23=0
    self.count24=0
    return
  
  def ojamarakka(self,aitefield):
    if aitefield.tokuten.atack >= 2100:
      self.haichi.append([0,0,0,0,0,0,0,0])
      self.haichi.append([0,0,0,0,0,0,0,0])
      self.haichi.append([0,0,0,0,0,0,0,0])
      self.haichi.append([0,0,0,0,0,0,0,0])
      self.haichi.append([0,0,0,0,0,0,0,0])
      aitefield.tokuten.atack -= 2100
      aitefield.tokuten.end += 2100
      for j in range(14,19):
        for i in range(1,7):
          self.haichi[j][i]=5
      self.sokurakka(19)
      self.haichi.pop(18)
      self.haichi.pop(17)
      self.haichi.pop(16)
      self.haichi.pop(15)
      self.haichi.pop(14)
      return 0
    else:
      self.haichi.append([0,0,0,0,0,0,0,0])
      self.haichi.append([0,0,0,0,0,0,0,0])
      self.haichi.append([0,0,0,0,0,0,0,0])
      self.haichi.append([0,0,0,0,0,0,0,0])
      self.haichi.append([0,0,0,0,0,0,0,0])
      y1 = aitefield.tokuten.atack // 70
      y2 = aitefield.tokuten.atack % 70
      aitefield.tokuten.atack = 0
      aitefield.tokuten.end += 70 * y1
      aitefield.tokuten.behind += y2
      if y1>24:
        for j in range(14,18):
          for i in range(1,7):
            self.haichi[j][i]=5
        o=random.sample(range(6),6)
        for i in range(y1-24):
          self.haichi[18][o[i]+1]=5
      elif y1>18:
        for j in range(14,17):
          for i in range(1,7):
            self.haichi[j][i]=5
        o=random.sample(range(6),6)
        for i in range(y1-18):
          self.haichi[17][o[i]+1]=5
      elif y1>12:
        for j in range(14,16):
          for i in range(1,7):
            self.haichi[j][i]=5
        o=random.sample(range(6),6)
        for i in range(y1-12):
          self.haichi[16][o[i]+1]=5
      elif y1>6:
        for j in range(14,15):
          for i in range(1,7):
            self.haichi[j][i]=5
        o=random.sample(range(6),6)
        for i in range(y1-6):
          self.haichi[15][o[i]+1]=5
      else:
        o=random.sample(range(6),6)
        for i in range(y1):
          self.haichi[14][o[i]+1]=5
      self.sokurakka(19)
      self.haichi.pop(18)
      self.haichi.pop(17)
      self.haichi.pop(16)
      self.haichi.pop(15)
      self.haichi.pop(14)
      return 0
  

  def rakka(self,y):
    count2=0
    while True:
      count=0
      for j in range(1,y):
        for i in range(1,7):
          if self.haichi[j][i]!=0 and self.haichi[j-1][i]==0:
            count+=1
            self.haichi[j-1][i]=self.haichi[j][i]
            self.haichi[j][i]=0
      count2+=1
      if count==0:
        break
      time.sleep(0.3)
    return count2
  
  def rakka_chigiri(self,y):
    count2=0
    while True:
      count=0
      for j in range(1,y):
        for i in range(1,7):
          if self.haichi[j][i]!=0 and self.haichi[j-1][i]==0:
            count+=1
            self.haichi[j-1][i]=self.haichi[j][i]
            self.haichi[j][i]=0
      count2+=1
      if count==0:
        break
      time.sleep(0.2)
    return count2
  
  def sokurakka(self,y):
    count2=0
    while True:
      count=0
      for j in range(1,y):
        for i in range(1,7):
          if self.haichi[j][i]!=0 and self.haichi[j-1][i]==0:
            count+=1
            self.haichi[j-1][i]=self.haichi[j][i]
            self.haichi[j][i]=0
      count2+=1
      if count==0:
        break
      time.sleep(0.003)
    time.sleep(0.4)
    return count2
  
 
  def renketu2(self,i,j):
    a=self.haichi[j][i]
    if a==0 or a==5 or a==11 or a==12 or a==13 or a==14  or a==15  or a==20:
      return 1
    if self.haichi[j][i]==1:
      self.count21+=1
      self.haichi[j][i]=11
    elif self.haichi[j][i]==2:
      self.count22+=1
      self.haichi[j][i]=12
    elif self.haichi[j][i]==3:
      self.count23+=1
      self.haichi[j][i]=13
    elif self.haichi[j][i]==4:
      self.count24+=1
      self.haichi[j][i]=14
    if a==self.haichi[j][i+1] :
      self.renketu2(i+1,j)
    elif self.haichi[j][i+1]==5:
      self.haichi[j][i+1]=15
    if a==self.haichi[j][i-1] :
      self.renketu2(i-1,j)
    elif self.haichi[j][i-1]==5:
      self.haichi[j][i-1]=15
    if j!=12 and j!=13 and j!=14 :
      if a==self.haichi[j+1][i]:
        self.renketu2(i,j+1)
      elif self.haichi[j+1][i]==5:
        self.haichi[j+1][i]=15
    if a==self.haichi[j-1][i]:
      self.renketu2(i,j-1)
    elif self.haichi[j-1][i]==5:
      self.haichi[j-1][i]=15
    return 1
 
 

  #renketukeshi
  def renketu3(self,i,j):
    a=self.haichi[j][i]
    if a==0 or a==5 or a==15 or a==1 or a==2 or a==3 or a==4 or a==20:
      return 1
    if self.haichi[j][i]==11:
      self.haichi[j][i]=0
    elif self.haichi[j][i]==12:
      self.haichi[j][i]=0
    elif self.haichi[j][i]==13:
      self.haichi[j][i]=0
    elif self.haichi[j][i]==14:
      self.haichi[j][i]=0
    if a==self.haichi[j][i+1]:
      self.renketu3(i+1,j)
    elif self.haichi[j][i+1]==15:
      self.haichi[j][i+1]=0
    if a==self.haichi[j][i-1] :
      self.renketu3(i-1,j)
    elif self.haichi[j][i-1]==15:
      self.haichi[j][i-1]=0
    if j!=12 and j!=13 and j!=14:
      if a==self.haichi[j+1][i]:
        self.renketu3(i,j+1)
      elif self.haichi[j+1][i]==15:
        self.haichi[j+1][i]=0
    if a==self.haichi[j-1][i]:
      self.renketu3(i,j-1)
    elif self.haichi[j-1][i]==15:
      self.haichi[j-1][i]=0
    return 1

  def renketukeshi2(self):
    count3=0
    count4=0
    count6=0
    irosuu=[0,0,0,0]
    for j in range(1,13):
      for i in range(1,7):
        y=[[s for s in m] for m in self.haichi] #jisakucopy.jisakucopy(self.haichi)
        self.count21=0
        self.count22=0
        self.count23=0
        self.count24=0
        self.renketu2(i,j)
        if self.count21>=4 or self.count22>=4 or self.count23>=4 or self.count24>=4:
          if self.count21>=4:
            irosuu[0]=1
          if self.count22>=4:
            irosuu[1]=1
          if self.count23>=4:
            irosuu[2]=1
          if self.count24>=4:
            irosuu[3]=1
          count31=self.count21+self.count22+self.count23+self.count24
          count3=self.count21+self.count22+self.count23+self.count24
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
          for l in range(1,13):
            for k in range(1,7):
              if self.haichi[l][k]==11 or self.haichi[l][k]==12 or self.haichi[l][k]==13 or self.haichi[l][k]==14 or self.haichi[l][k]==15:
                self.haichi[l][k]=0
        else:
          for l in range(1,13):
            for k in range(1,7):
              if self.haichi[l][k]==11 or self.haichi[l][k]==12 or self.haichi[l][k]==13 or self.haichi[l][k]==14 or self.haichi[l][k]==15:
                self.haichi[l][k]=y[l][k]
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


  def rensa(self,aitefield):
    j=self.renketukeshi2()
    if j[0]!=0:
      self.rensa_c+=1
    count=0
    if self.rensa_c==1:
      count=0
    elif self.rensa_c==2:
      count=8
    elif self.rensa_c==3:
      count=16
    elif self.rensa_c==4:
      count=32
    elif self.rensa_c==5:
      count=64
    elif self.rensa_c==6:
      count=96
    elif self.rensa_c==7:
      count=128
    elif self.rensa_c==8:
      count=160
    elif self.rensa_c==9:
      count=192
    elif self.rensa_c==10:
      count=224
    elif self.rensa_c==11:
      count=256
    elif self.rensa_c==12:
      count=288
    elif self.rensa_c==13:
      count=320
    elif self.rensa_c==14:
      count=352
    elif self.rensa_c==15:
      count=384
    elif self.rensa_c==16:
      count=416
    elif self.rensa_c==17:
      count=448
    elif self.rensa_c==18:
      count=480
    elif self.rensa_c==19:
      count=512
    k=count+j[1]+j[2]
    if k==0:
      k=1

    rensatokuten = j[0] * k * 10
    self.tokuten.hyouji += rensatokuten
    self.tokuten.sousai(aitefield.tokuten,rensatokuten)
    """
    if aitefield.counttotal==0 and aitefield.counttotal_a==0:
      self.counttotal+=j[0]*k*10
      self.counttotal2+=j[0]*k*10
      if j[0]!=0 and self.zenkeshihyouji==1:
        self.counttotal+=2100
        self.zenkeshihyouji=0
      if j[0]!=0 and self.counttotal_r!=0:
        self.counttotal+=self.counttotal_r
        self.counttotal_r=0
    elif aitefield.counttotal==0:
      aitefield.counttotal_a-=j[0]*k*10
      self.counttotal2+=j[0]*k*10
      if j[0]!=0 and self.zenkeshihyouji==1:
        aitefield.counttotal_a-=2100
        self.zenkeshihyouji=0
      if j[0]!=0 and self.counttotal_r!=0:
        aitefield.counttotal_a-=self.counttotal_r
        self.counttotal_r=0
      if aitefield.counttotal_a<0:
        self.counttotal-=aitefield.counttotal_a
        aitefield.counttotal_a=0
    else:
      aitefield.counttotal-=j[0]*k*10
      self.counttotal2+=j[0]*k*10
      if j[0]!=0 and self.zenkeshihyouji==1:
        aitefield.counttotal-=2100
        self.zenkeshihyouji=0
      if j[0]!=0 and self.counttotal_r!=0:
        aitefield.counttotal-=self.counttotal_r
        self.counttotal_r=0
      if aitefield.counttotal<0:
        aitefield.counttotal_a-=aitefield.counttotal
        aitefield.counttotal=0
      if aitefield.counttotal_a<0:
        self.counttotal-=aitefield.counttotal_a
        aitefield.counttotal_a=0
    """
    if j[0]!=0:
      self.zenkeshihyouji = 0
      time.sleep(1.3)
    aa=self.rakka(14)
    if aa==1:
      return 1
    self.rensa(aitefield)


class AIField(Field):

  def __init__(self,haichi):
    self.haichi=[[s for s in m] for m in haichi] #jisakucopy.jisakucopy(haichi)
    self.ojama=[0,0,0,0,0,0]
    self.counttotal=0
    self.counttotal2=0
    self.counttotal_r=0
    self.counttotal_a=0
    self.zenkeshihyouji=0
    self.rensa_c=0
    self.haichi_c=0
    self.renketu_c=0
    return

  def rakka(self,y):
    count2=0
    while True:
      count=0
      for j in range(1,y):
        for i in range(1,7):
          if self.haichi[j][i]!=0 and self.haichi[j-1][i]==0:
            count+=1
            self.haichi[j-1][i]=self.haichi[j][i]
            self.haichi[j][i]=0
      count2+=1
      if count==0:
        break
    return count2
  def rakka_chigiri(self,y):
    count2=0
    while True:
      count=0
      for j in range(1,y):
        for i in range(1,7):
          if self.haichi[j][i]!=0 and self.haichi[j-1][i]==0:
            count+=1
            self.haichi[j-1][i]=self.haichi[j][i]
            self.haichi[j][i]=0
      count2+=1
      if count==0:
        break
    return count2

  def puyooki(self,puyo,x):
    if x==1:
      self.haichi[13][1]=puyo.puyo2iro
      self.haichi[14][1]=puyo.puyo1iro
    elif x==2:
      self.haichi[13][2]=puyo.puyo2iro
      self.haichi[14][2]=puyo.puyo1iro
    elif x==3:
      self.haichi[13][3]=puyo.puyo2iro
      self.haichi[14][3]=puyo.puyo1iro
    elif x==4:
      self.haichi[13][4]=puyo.puyo2iro
      self.haichi[14][4]=puyo.puyo1iro
    elif x==5:
      self.haichi[13][5]=puyo.puyo2iro
      self.haichi[14][5]=puyo.puyo1iro
    elif x==6:
      self.haichi[13][6]=puyo.puyo2iro
      self.haichi[14][6]=puyo.puyo1iro
    elif x==7:
      self.haichi[14][1]=puyo.puyo2iro
      self.haichi[13][1]=puyo.puyo1iro
    elif x==8:
      self.haichi[14][2]=puyo.puyo2iro
      self.haichi[13][2]=puyo.puyo1iro
    elif x==9:
      self.haichi[14][3]=puyo.puyo2iro
      self.haichi[13][3]=puyo.puyo1iro
    elif x==10:
      self.haichi[14][4]=puyo.puyo2iro
      self.haichi[13][4]=puyo.puyo1iro
    elif x==11:
      self.haichi[14][5]=puyo.puyo2iro
      self.haichi[13][5]=puyo.puyo1iro
    elif x==12:
      self.haichi[14][6]=puyo.puyo2iro
      self.haichi[13][6]=puyo.puyo1iro
    elif x==13:
      self.haichi[13][1]=puyo.puyo2iro
      self.haichi[13][2]=puyo.puyo1iro
    elif x==14:
      self.haichi[13][2]=puyo.puyo2iro
      self.haichi[13][3]=puyo.puyo1iro
    elif x==15:
      self.haichi[13][3]=puyo.puyo2iro
      self.haichi[13][4]=puyo.puyo1iro
    elif x==16:
      self.haichi[13][4]=puyo.puyo2iro
      self.haichi[13][5]=puyo.puyo1iro
    elif x==17:
      self.haichi[13][5]=puyo.puyo2iro
      self.haichi[13][6]=puyo.puyo1iro
    elif x==18:
      self.haichi[13][2]=puyo.puyo2iro
      self.haichi[13][1]=puyo.puyo1iro
    elif x==19:
      self.haichi[13][3]=puyo.puyo2iro
      self.haichi[13][2]=puyo.puyo1iro
    elif x==20:
      self.haichi[13][4]=puyo.puyo2iro
      self.haichi[13][3]=puyo.puyo1iro
    elif x==21:
      self.haichi[13][5]=puyo.puyo2iro
      self.haichi[13][4]=puyo.puyo1iro
    elif x==22:
      self.haichi[13][6]=puyo.puyo2iro
      self.haichi[13][5]=puyo.puyo1iro
    return

  #subetenopuyonorenketu
  def renketusirabe(self):
    count3=0
    count4=0
    count5=0
    y=[[s for s in m] for m in self.haichi] #jisakucopy.jisakucopy(self.haichi)
    for i in range(1,7):
      for j in range(1,13):
        if self.haichi[j][i]==0:
          break
        count4+=j**2
        count5+=(i-3.5)**2
        if self.haichi[j][i]==1 or self.haichi[j][i]==2 or self.haichi[j][i]==3 or self.haichi[j][i]==4:
          self.count21=0
          self.count22=0
          self.count23=0
          self.count24=0
          self.renketu2(i,j)
          '''
          for k in range(1,7):
            for l in range(1,13):
              if self.haichi[l][k]==0:
                break
              if self.haichi[l][k]==11:
                self.haichi[l][k]=20
                count4+=l**2
                count5+=(k-3.5)**2
              elif self.haichi[l][k]==12:
                self.haichi[l][k]=20
                count4+=l**2
                count5+=(k-3.5)**2
              elif self.haichi[l][k]==13:
                self.haichi[l][k]=20
                count4+=l**2
                count5+=(k-3.5)**2
              elif self.haichi[l][k]==14:
                self.haichi[l][k]=20
                count4+=l**2
                count5+=(k-3.5)**2
          '''
          count3=count3+self.count21**2+self.count22**2+self.count23**2+self.count24**2
    self.haichi=[[s for s in m] for m in y] #jisakucopy.jisakucopy(y)
    return count3,count4,int(count5)


  
  #oitapuyokaranorenketusuu,takasa
  def renketusirabe4(self,puyo):
    count3=0
    count4=0
    y=[[s for s in m] for m in self.haichi] #jisakucopy.jisakucopy(self.haichi)
    self.count21=0
    self.count22=0
    self.count23=0
    self.count24=0
    self.renketu2(puyo.puyo1x,puyo.puyo1y)
    count3=count3+self.count21**2+self.count22**2+self.count23**2+self.count24**2
    if self.haichi[puyo.puyo2y][puyo.puyo2x]==1 or self.haichi[puyo.puyo2y][puyo.puyo2x]==2 or self.haichi[puyo.puyo2y][puyo.puyo2x]==3 or self.haichi[puyo.puyo2y][puyo.puyo2x]==4:
      self.count21=0
      self.count22=0
      self.count23=0
      self.count24=0
      self.renketu2(puyo.puyo2x,puyo.puyo2y)
      count3=count3+self.count21**2+self.count22**2+self.count23**2+self.count24**2
    self.haichi=[[s for s in m] for m in y] #jisakucopy.jisakucopy(y)
    return count3,puyo.puyo1y**2+puyo.puyo2y**2
  
  #4renketuhadame
  def renketusirabe5(self,puyo):
    count3=0
    count4=0
    y=[[s for s in m] for m in self.haichi] #jisakucopy.jisakucopy(self.haichi)
    self.count21=0
    self.count22=0
    self.count23=0
    self.count24=0
    self.renketu2(puyo.puyo1x,puyo.puyo1y)
    if self.count21>=4 or self.count22>=4 or self.count23>=4 or self.count24>=4:
      self.haichi=[[s for s in m] for m in y] #jisakucopy.jisakucopy(y)
      return True
    if self.haichi[puyo.puyo2y][puyo.puyo2x]==1 or self.haichi[puyo.puyo2y][puyo.puyo2x]==2 or self.haichi[puyo.puyo2y][puyo.puyo2x]==3 or self.haichi[puyo.puyo2y][puyo.puyo2x]==4:
      self.count21=0
      self.count22=0
      self.count23=0
      self.count24=0
      self.renketu2(puyo.puyo2x,puyo.puyo2y)
      if self.count21>=4 or self.count22>=4 or self.count23>=4 or self.count24>=4:
        self.haichi=[[s for s in m] for m in y] #jisakucopy.jisakucopy(y)
        return True
    self.haichi=[[s for s in m] for m in y] #jisakucopy.jisakucopy(y)
    return False

  def renketusirabe6(self,i,j):
    y=[[s for s in m] for m in self.haichi] #jisakucopy.jisakucopy(self.haichi)
    self.count21=0
    self.count22=0
    self.count23=0
    self.count24=0
    self.renketu2(i,j)
    if self.count21>=4 or self.count22>=4 or self.count23>=4 or self.count24>=4:
      self.renketu3(i,j)
#      for k in range(1,7):
#        for l in range(1,13):
#          if self.haichi[l][k]==0:
#            break
#          if self.haichi[l][k]==11 or self.haichi[l][k]==12 or self.haichi[l][k]==13 or self.haichi[l][k]==14 or self.haichi[l][k]==15:
#            self.haichi[l][k]=0
      return True
    else:
      for k in range(1,7):
        for l in range(1,13):
          if self.haichi[l][k]==0:
            break
          if self.haichi[l][k]==11:
            self.haichi[l][k]=1
          elif  self.haichi[l][k]==12:
            self.haichi[l][k]=2
          elif  self.haichi[l][k]==13:
            self.haichi[l][k]=3
          elif  self.haichi[l][k]==14:
            self.haichi[l][k]=4
      return False


  #renketukeshi
  def renketukeshi2(self):
    count3=0
    for j in range(1,13):
      for i in range(1,7):
        if self.haichi[j][i]==0 or self.haichi[j][i]==11 or self.haichi[j][i]==12 or self.haichi[j][i]==13 or  self.haichi[j][i]==14:
          continue
        self.count21=0
        self.count22=0
        self.count23=0
        self.count24=0
        self.renketu2(i,j)
        if self.count21>=4 or self.count22>=4 or self.count23>=4 or self.count24>=4:
          count3+=self.count21+self.count22+self.count23+self.count24
          self.renketu3(i,j)
    for l in range(1,13):
      for k in range(1,7):
        if self.haichi[l][k]==0:
          continue
        if self.haichi[l][k]==11:
          self.haichi[l][k]=1
        elif self.haichi[l][k]==12: 
          self.haichi[l][k]=2
        elif self.haichi[l][k]==13:
          self.haichi[l][k]=3
        elif self.haichi[l][k]==14:
          self.haichi[l][k]=4
        elif self.haichi[l][k]==15:
          self.haichi[l][k]=5

    return count3

  #renketukeshi_sannsyou
  def renketukeshi2_2(self):
    count3=0
    for y,j in enumerate(self.haichi):
      for x,i in enumerate(j):
        if i==0 or i==11 or i==12 or i==13 or i==14 or i==15 or 1==20:
          continue
        self.count21=0
        self.count22=0
        self.count23=0
        self.count24=0
        self.renketu2(x,y)
        if self.count21>=4 or self.count22>=4 or self.count23>=4 or self.count24>=4:
          count3+=self.count21+self.count22+self.count23+self.count24
          self.renketu3(x,y)
    for l in self.haichi:
      for k in l:
        if k==0:
          continue
        if k==11:
          k=1
        elif k==12: 
          k=2
        elif k==13:
          k=3
        elif k==14:
          k=4
        elif k==15:
          k=5

    return count3


  def renketukeshi3(self,i,j):
    y=[[s for s in m] for m in self.haichi] #jisakucopy.jisakucopy(self.haichi)
    self.count21=0
    self.count22=0
    self.count23=0
    self.count24=0
    self.renketu2(i,j)
    if self.count21>=3 or self.count22>=3 or self.count23>=3 or self.count24>=3: 
      for k in range(1,7):
        for l in range(1,13):
          if self.haichi[l][k]==0:
            break
          if self.haichi[l][k]==11 or self.haichi[l][k]==12 or self.haichi[l][k]==13 or self.haichi[l][k]==14 or self.haichi[l][k]==15:
            self.haichi[l][k]=0
    else:
      for k in range(1,7):
        for l in range(1,13):
          if self.haichi[l][k]==0:
            break
          if self.haichi[l][k]==11 or self.haichi[l][k]==12 or self.haichi[l][k]==13 or self.haichi[l][k]==14 or self.haichi[l][k]==15:
            self.haichi[l][k]=y[l][k]

    return 1

  
  def sokurensa(self):
    j=self.renketukeshi2()
    if j>=4:
      self.renketu_c+=j-4
    if j!=0:
      self.rensa_c+=1
    aa=self.rakka(14)
    if aa==1:
      return 1
    self.sokurensa()
  
  def rensashirabe(self):
    kekka_rensasuu=np.zeros((6,12),dtype=np.int)
    self.renketu_c=0
    for i in range(1,7):
      for j in range(1,13):
        if self.haichi[j][i]==0:
          break
        q=[[s for s in m] for m in self.haichi] #jisakucopy.jisakucopy(self.haichi)
        self.rensa_c=0
        if self.hakkatensirabe(i,j):
          continue
        self.renketukeshi3(i,j) 
        if self.count21<3 and self.count22<3 and self.count23<3 and self.count24<3:
          self.haichi=[[s for s in m] for m in q] #jisakucopy.jisakucopy(q)
          continue
        self.rakka(14)
        self.sokurensa()
        kekka_rensasuu[i-1][j-1]=self.rensa_c
        self.haichi=[[s for s in m] for m in q] #jisakucopy.jisakucopy(q)
    return kekka_rensasuu.max()

  def rensashirabe2(self):
    kekka_rensasuu=np.zeros((6,12),dtype=np.int)
    self.renketu_c=0
    q=[[s for s in m] for m in self.haichi] #jisakucopy.jisakucopy(self.haichi)
    for i in range(1,7):
      for j in range(12,0,-1):
        if self.haichi[j][i]!=0:
          break
        if self.haichi[j-2][i]==0 or self.haichi[j-2][i]==20:
          continue
        if self.haichi[j-1][i]==0 and (self.haichi[j][i-1]==0 or self.haichi[j][i-1]==20) and (self.haichi[j][i+1]==0 or self.haichi[j][i+1]==20):
          continue
        self.rensa_c=0
        for k in range(1,5):
          self.haichi[j][i]=k
          if self.renketusirabe6(i,j):
            self.rakka(14)
            self.sokurensa()
            kekka_rensasuu[i-1][j-1]=self.rensa_c
            self.haichi=[[s for s in m] for m in q] #jisakucopy.jisakucopy(q)
          else:
            self.haichi[j][i]=0
    return kekka_rensasuu.max()
          
  def shin_rensashirabe(self):
    q=[[s for s in m] for m in self.haichi] #jisakucopy.jisakucopy(self.haichi)
    self.rensa_c=0
    self.sokurensa()
    self.haichi=[[s for s in m] for m in q] #jisakucopy.jisakucopy(q)
    return self.rensa_c

  def hakkatensirabe(self,i,j):
    if self.haichi[j][i-1]==0 and self.haichi[j-2][i-1]!=0:
      return False
    elif self.haichi[j+1][i]==0:
      return False
    elif self.haichi[j][i+1]==0 and self.haichi[j-2][i+1]!=0:
      return False
    else:
      return True
    
  def zenkeshishirabe(self):
    for i in range(1,7):
      if self.haichi[1][i]!=0:
        return False
    return True
  
  def chissokushirabe(self):
    kekka=0
    for j in range(11,14):
      for i in range(2,5):
        if self.haichi[j][i]!=0:
          kekka+=(10-(3-i)**2)*j**2*100
    return kekka
 
