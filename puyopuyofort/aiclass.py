import random
import numpy as np
from fieldclass import AIField
from puyoclass import AIPuyo
import time
import jisakucopy
from fortcall import Fort


class CPU():  
 
  def __init__(self):
    self.cpu_c=0
    self.cpu_sousa_c=1

  #random
  def ai1(self,field,puyo):
    return random.randint(1,22)

  #1rensa
  def ai2(self,field,puyo):
    kekka=np.zeros((2,22),dtype=np.int)
    for i in range(22):
      aifield=AIField(field)
      a=self.cpu_idouhantei(aifield,puyo,i+1)
      if a==1:
        aifield.puyooki(puyo,i+1)
        aifield.rakka(15)
        b=aifield.renketusirabe(i+1)
        kekka[0][i]=b[0]
        kekka[1][i]=b[1]
    renketumax=kekka[0].max()
    for i in range(22):
      if kekka[0][i]!=renketumax:
        kekka[1][i]=100000
    return kekka[1].argmin()+1

  #1rensakairyou
  def ai3(self,field,puyo):
    kekka=np.zeros((2,22),dtype=np.int)
    aipuyo=AIPuyo()
    for i in range(22):
      aifield=AIField(field)
      aipuyo.syokika(puyo)
      a=self.cpu_idouhantei(aifield,aipuyo,i+1)
      if a==1:
        aipuyo.puyooki(i+1)
        aipuyo.rakka(aifield.haichi)
        b=aifield.renketusirabe4(aipuyo)
        kekka[0][i]=b[0]
        kekka[1][i]=b[1]
    renketumax=kekka[0].max()
    for i in range(22):
      if kekka[0][i]!=renketumax:
        kekka[1][i]=100000
    return kekka[1].argmin()+1
   
  #rensa
  def ai4(self,haichi,puyo):
    kekka=np.zeros((3,22),dtype=np.int)
    aipuyo=AIPuyo()
    for i in range(22):
      aifield=AIField(haichi)
      aipuyo.syokika(puyo)
      a=self.cpu_idouhantei(aifield,aipuyo,i+1)
      if a==1:
        aipuyo.puyooki(i+1)
        aipuyo.rakka(aifield.haichi)
        if aifield.shin_rensashirabe()>=5:
          return i+1
        if aifield.renketusirabe5(aipuyo):
          continue
        b=aifield.renketusirabe4(aipuyo)
        kekka[0][i]=b[0]
        kekka[1][i]=b[1]
        kekka[2][i]=aifield.rensashirabe()
    rensamax=kekka[2].max()
    for i in range(22):
      if kekka[2][i]!=rensamax:
        kekka[0][i]=0
    renketumax=kekka[0].max()
    for i in range(22):
      if kekka[0][i]!=renketumax:
        kekka[1][i]=100000
    return kekka[1].argmin()+1


  #rensa
  def ai5(self,haichi,puyo_1,puyo_2):
    kekka=np.zeros((4,22,22),dtype=np.int)
    aipuyo_1=AIPuyo()
    aipuyo_2=AIPuyo()
    for i in range(22):
      aifield=AIField(haichi)
      aipuyo_1.syokika(puyo_1)
      idouhantei_c=self.cpu_idouhantei(aifield,aipuyo_1,i+1)
      if idouhantei_c!=1:
        continue
      aipuyo_1.puyooki(i+1)
      aipuyo_1.rakka(aifield.haichi)
      if aifield.shin_rensashirabe()>=5:
        return i+1
      if aifield.renketusirabe5(aipuyo_1):
         aifield.sokurensa()
#        kekka[1][i][0]=1
#        continue
#      kekka[3][i][0]=aifield.rensashirabe()
      for j in range(22):
        aipuyo_2.syokika(puyo_2)
        y=[[s for s in m] for m in aifield.haichi] #jisakucopy.jisakucopy(aifield)
        idouhantei_c_2=self.cpu_idouhantei(aifield,aipuyo_2,j+1)
        if idouhantei_c_2!=1:
          continue
        aipuyo_2.puyooki(j+1)
        aipuyo_2.rakka(aifield.haichi)
        if aifield.renketusirabe5(aipuyo_2):
          aifield.sokurensa() 
#          aifield.haichi=copy.deepcopy(y)
#          kekka[1][i][j]=1
#          continue
        b=aifield.renketusirabe()
        kekka[0][i][j]=b[0]
        kekka[1][i][j]=1000000-b[1]
        kekka[2][i][j]=aifield.rensashirabe()
        aifield.haichi=[[s for s in m] for m in y] #jisakucopy.jisakucopy(y)
#    rensamax_1=kekka[3].max()
    rensamax=kekka[2].max()
#    if rensamax_1>=rensamax_2:
#      rensamax=rensamax_1
#    else:
#      rensamax=rensamax_2
    for i in range(22):
      for j in range(22):
        if kekka[2][i][j]!=rensamax:# kekka[3][i][0]!=rensamax:
          kekka[0][i][j]=0
    renketumax=kekka[0].max()
    for i in range(22):
      for j in range(22):
        if kekka[0][i][j]!=renketumax:
          kekka[1][i][j]=0
    c=kekka[1].max(axis=1)
    return c.argmax()+1

  #rensa hyoukakannsuugata
  def ai6(self,haichi,puyo_1,puyo_2):
    kekka=np.zeros((22,22),dtype=np.int)
    aipuyo_1=AIPuyo()
    aipuyo_2=AIPuyo()
    for i in range(22):
      aifield=AIField(haichi)
      aipuyo_1.syokika(puyo_1)
      idouhantei_c=self.cpu_idouhantei(aifield,aipuyo_1,i+1)
      if idouhantei_c!=1:
        kekka[i]-=1000000
        continue
      aipuyo_1.puyooki(i+1)
      aipuyo_1.rakka(aifield.haichi)
      if aifield.shin_rensashirabe()>=8:
        return i+1
      if aifield.renketusirabe5(aipuyo_1):
        aifield.sokurensa()
      for j in range(22):
        aipuyo_2.syokika(puyo_2)
        y=[[s for s in m] for m in aifield.haichi] #jisakucopy.jisakucopy(aifield.haichi)
        idouhantei_c_2=self.cpu_idouhantei(aifield,aipuyo_2,j+1)
        if idouhantei_c_2!=1:
          kekka[i][j]-=10000
          continue
        aipuyo_2.puyooki(j+1)
        aipuyo_2.rakka(aifield.haichi)
        if aifield.renketusirabe5(aipuyo_2):
          aifield.sokurensa()
        b=aifield.renketusirabe()
        kekka[i][j]+=b[0]*1000
        kekka[i][j]-=b[1]
        kekka[i][j]+=aifield.rensashirabe()*1000000
        aifield.haichi=[[s for s in m] for m in y] #jisakucopy.jisakucopy(y)
    kekka2=kekka.max(axis=1)
    return kekka2.argmax()+1

  #rensa rensakouritu
  def ai7(self,haichi,puyo_1,puyo_2):
    kekka=np.zeros((22,22),dtype=np.int)
    aipuyo_1=AIPuyo()
    aipuyo_2=AIPuyo()
    for i in range(22):
      aifield=AIField(haichi)
      aipuyo_1.syokika(puyo_1)
      idouhantei_c=self.cpu_idouhantei(aifield,aipuyo_1,i+1)
      if idouhantei_c!=1:
        kekka[i]-=1000000
        continue
      aipuyo_1.puyooki(i+1)
      aipuyo_1.rakka(aifield.haichi)
      if aifield.shin_rensashirabe()>=5:
        return i+1
      if aifield.renketusirabe5(aipuyo_1):
        aifield.sokurensa()
      for j in range(22):
        aipuyo_2.syokika(puyo_2)
        y=[[s for s in m] for m in aifield.haichi] #jisakucopy.jisakucopy(aifield.haichi)
        idouhantei_c_2=self.cpu_idouhantei(aifield,aipuyo_2,j+1)
        if idouhantei_c_2!=1:
          kekka[i][j]-=10000
          continue
        aipuyo_2.puyooki(j+1)
        aipuyo_2.rakka(aifield.haichi)
        if aifield.renketusirabe5(aipuyo_2):
          aifield.sokurensa()
        b=aifield.renketusirabe()
        kekka[i][j]+=b[0]*1000
        kekka[i][j]-=b[1]*4
        kekka[i][j]+=b[2]
        kekka[i][j]+=aifield.rensashirabe()*1000000
        kekka[i][j]-=(aifield.renketu_c**2)*1000
        aifield.haichi=[[s for s in m] for m in y] #jisakucopy.jisakucopy(y)
    kekka2=kekka.max(axis=1)
    return kekka2.argmax()+1

  #aitenohakkakanti
  def ai8(self,field,field2,puyo_1,puyo_2):
    kekka=np.zeros((22,22),dtype=np.int)
    aipuyo_1=AIPuyo()
    aipuyo_2=AIPuyo()
    aiterensa_c=0
    fort=Fort()
    fok=0
    if field2.counttotal_a!=0 or field2.counttotal!=0:
      aifield_aite=AIField(field2.haichi)
      aifield_aite.rakka(14)
      aiterensa_c+=field2.rensa_c+aifield_aite.shin_rensashirabe()
    for i in range(22):
      aifield=AIField(field.haichi)
      aipuyo_1.syokika(puyo_1)
      idouhantei_c=self.cpu_idouhantei(aifield,aipuyo_1,i+1)
      if idouhantei_c!=1:
        kekka[i]-=1000000
        continue
      aipuyo_1.puyooki(i+1)
      aipuyo_1.rakka(aifield.haichi)
      if aiterensa_c>=1:
         o=aifield.shin_rensashirabe()
         if o>aiterensa_c:
          aiterensa_c=0
          return i+1
      if aifield.shin_rensashirabe()>=7:
        return i+1
      if aifield.renketusirabe5(aipuyo_1):
        aifield.sokurensa()
      for j in range(22):
        aipuyo_2.syokika(puyo_2)
        y=[[s for s in m] for m in aifield.haichi] #jisakucopy.jisakucopy(aifield.haichi)
        idouhantei_c_2=self.cpu_idouhantei(aifield,aipuyo_2,j+1)
        if idouhantei_c_2!=1:
          kekka[i][j]-=10000
          continue
        aipuyo_2.puyooki(j+1)
        aipuyo_2.rakka(aifield.haichi)
        if aifield.renketusirabe5(aipuyo_2):
          aifield.sokurensa()
        b=aifield.renketusirabe()
        kekka[i][j]+=b[0]*1000
        kekka[i][j]-=b[1]*4
        kekka[i][j]+=b[2]
        fok=fort.call_fortran(aifield.haichi)
        kekka[i][j]+=fok*1000000
        kekka[i][j]-=(aifield.renketu_c**2)*1000
        aifield.haichi=[[s for s in m] for m in y] #jisakucopy.jisakucopy(y)
    kekka2=kekka.max(axis=1)
    return kekka2.argmax()+1


  def cpu_os(self):
#    l=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1)
#    return random.choice(l)
    return 1

  def cpu_idouhantei(self,field,puyo,x):


    if x==1:
      if field.haichi[13][1]!=0 or field.haichi[13][2]!=0:
        return 0
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x-1]!=0:
        return 0
      elif  field.haichi[puyo.puyo2y][2]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0: 
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          return 1
        else:
          return 0
      elif field.haichi[puyo.puyo2y][1]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0 and field.haichi[puyo.puyo2y][4]==0:
          return 1
        else:
          return 0
      else: 
        return 1


    elif x==2:
      if field.haichi[13][2]!=0:
        return 0
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x-1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][2]!=0: 
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          return 1
        else:
          return 0
      else:
        return 1


    elif x==3:
      if field.haichi[10][3]!=0:
        y=jisakucopy.jisakucopy(field.haichi)
        puyo.puyooki(3)
        puyo.rakka(field.haichi)
        field.sokurensa()
        if field.haichi[12][3]!=0:
          field.haichi=jisakucopy.jisakucopy(y)
          return 0
        else:
          field.haichi=jisakucopy.jisakucopy(y)
          return 1
      else:
        return 1


    elif x==4:
      if field.haichi[13][4]!=0:
        return 0
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1 
        elif field.haichi[puyo.puyo2y-1][2]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          return 1
        else:
          return 0
      else:
        return 1


    elif x==5:
      if field.haichi[13][5]!=0 or field.haichi[13][4]!=0:
        return 0
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]!=0: 
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          return 1
        else:
          return 0
      elif field.haichi[puyo.puyo2y][5]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0 and field.haichi[puyo.puyo2y][2]==0:
          return 1
        else:
          return 0
      else:
        return 1 


    elif x==6:
      if field.haichi[13][5]!=0 or field.haichi[13][4]!=0 or field.haichi[13][6]!=0:
        return 0
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]!=0: 
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          return 1
        else:
          return 0
      elif field.haichi[puyo.puyo2y][5]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0 and field.haichi[puyo.puyo2y][2]==0:
          return 1
        else:
          return 0
      elif field.haichi[puyo.puyo2y][6]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][5]!=0:
          return 1
        else:
          return 0
      else:
        return 1


    elif x==7:
      if field.haichi[12][1]!=0 or field.haichi[13][2]!=0:
        return 0
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x-1]!=0:
        return 0
      elif  field.haichi[puyo.puyo2y][2]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0: 
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          return 1
        else:
          return 0
      elif field.haichi[puyo.puyo2y][1]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0 and field.haichi[puyo.puyo2y][4]==0:
          return 1
        else:
          return 0
      else: 
        return 1


    elif x==8:
      if field.haichi[12][2]!=0:
        return 0
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x-1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][2]!=0: 
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          return 1
        else:
          return 0
      else:
        return 1


    elif x==9:
      if field.haichi[10][3]!=0:
        y=jisakucopy.jisakucopy(field.haichi)
        puyo.puyooki(3)
        puyo.rakka(field.haichi)
        field.sokurensa()
        if field.haichi[12][3]!=0:
          field.haichi=jisakucopy.jisakucopy(y)
          return 0
        else:
          field.haichi=jisakucopy.jisakucopy(y)
          return 1
      else:
        return 1


    elif x==10:
      if field.haichi[12][4]!=0:
        return 0
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1 
        elif field.haichi[puyo.puyo2y-1][2]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          return 1
        else:
          return 0
      else:
        return 1


    elif x==11:
      if field.haichi[12][5]!=0 or field.haichi[13][4]!=0:
        return 0
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]!=0: 
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          return 1
        else:
          return 0
      elif field.haichi[puyo.puyo2y][5]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0 and field.haichi[puyo.puyo2y][2]==0:
          return 1
        else:
          return 0
      else:
        return 1 


    elif x==12:
      if field.haichi[12][6]!=0 or field.haichi[13][5]!=0 or field.haichi[13][4]!=0:
        return 0
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]!=0: 
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          return 1
        else:
          return 0
      elif field.haichi[puyo.puyo2y][5]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0 and field.haichi[puyo.puyo2y][2]==0:
          return 1
        else:
          return 0
      elif field.haichi[puyo.puyo2y][6]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][5]!=0:
          return 1
        else:
          return 0
      else:
        return 1


    elif x==13:
      if field.haichi[13][1]!=0 or field.haichi[13][2]!=0:
        return 0
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x-1]!=0:
        return 0
      elif  field.haichi[puyo.puyo2y][2]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0: 
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          return 1
        else:
          return 0
      elif field.haichi[puyo.puyo2y][1]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0 and field.haichi[puyo.puyo2y][4]==0:
          return 1
        else:
          return 0
      else: 
        return 1


    elif x==14:
      if field.haichi[13][2]!=0: 
        return 0
      elif field.haichi[11][3]!=0:
        y=jisakucopy.jisakucopy(field.haichi)
        puyo.puyooki(3)
        puyo.rakka(field.haichi)
        field.sokurensa()
        if field.haichi[12][3]!=0:
          field.haichi=jisakucopy.jisakucopy(y)
          return 0
        else:
          field.haichi=jisakucopy.jisakucopy(y)
          return 1
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x-1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][2]!=0: 
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          return 1
        else:
          return 0
      else:
        return 1


    elif x==15:
      if field.haichi[13][4]!=0:
        return 0
      elif field.haichi[11][3]!=0: 
        y=jisakucopy.jisakucopy(field.haichi)
        puyo.puyooki(3)
        puyo.rakka(field.haichi)
        field.sokurensa()
        if field.haichi[12][3]!=0:
          field.haichi=jisakucopy.jisakucopy(y)
          return 0
        else:
          field.haichi=jisakucopy.jisakucopy(y)
          return 1
      elif field.haichi[puyo.puyo2y][4]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          return 1
        else:
          return 0
      else:
        return 1


    elif x==16:
      if field.haichi[13][4]!=0 or field.haichi[13][5]!=0:
        return 0
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1 
        elif field.haichi[puyo.puyo2y-1][2]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          return 1
        else:
          return 0
      elif field.haichi[puyo.puyo2y][5]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y][2]==0:
          if field.haichi[puyo.puyo2y-1][2]!=0: 
            return 1
          elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
            return 1
          else:
            return 0
        else:
          return 0
      else:
        return 1


    elif x==17:
      if field.haichi[13][5]!=0 or field.haichi[13][4]!=0 or field.haichi[13][6]!=0:
        return 0
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]!=0: 
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          return 1
        else:
          return 0
      elif field.haichi[puyo.puyo2y][5]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0 and field.haichi[puyo.puyo2y][2]==0:
          return 1
        else:
          return 0
      elif field.haichi[puyo.puyo2y][6]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][5]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0 and field.haichi[puyo.puyo2y][2]==0:
          return 1
        else:
          return 0 
      else:
        return 1 


    elif x==18:
      if field.haichi[13][2]!=0 or field.haichi[13][1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x-1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][2]!=0: 
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          return 1
        else:
          return 0
      elif field.haichi[puyo.puyo2y][1]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0:
          return 1
        elif field.haichi[puyo.puyo2y][4]==0:
          if field.haichi[puyo.puyo2y-1][4]!=0:
            return 1
          elif field.haichi[puyo.puyo2y][5]==0 and field.haichi[puyo.puyo2y-1][5]!=0:
            return 1
          else:
            return 0
      else:
        return 1


    elif x==19:
      if field.haichi[13][2]!=0:
        return 0
      if field.haichi[11][3]!=0: 
        y=jisakucopy.jisakucopy(field.haichi)
        puyo.puyooki(3)
        puyo.rakka(field.haichi)
        field.sokurensa()
        if field.haichi[12][3]!=0:
          field.haichi=jisakucopy.jisakucopy(y)
          return 0
        else:
          field.haichi=jisakucopy.jisakucopy(y)
          return 1
      elif field.haichi[puyo.puyo2y][2]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y][5]==0:
          if field.haichi[puyo.puyo2y-1][5]!=0: 
            return 1
          elif field.haichi[puyo.puyo2y-1][6]!=0 and field.haichi[puyo.puyo2y][6]==0:
            return 1
          else:
            return 0 
        else:
          return 0

      else:
        return 1


    elif x==20:
      if field.haichi[13][4]!=0: 
        return 0
      elif field.haichi[11][3]!=0:
        y=jisakucopy.jisakucopy(field.haichi)
        puyo.puyooki(3)
        puyo.rakka(field.haichi)
        field.sokurensa()
        if field.haichi[12][3]!=0:
          field.haichi=jisakucopy.jisakucopy(y)
          return 0
        else:
          field.haichi=jisakucopy.jisakucopy(y)
          return 1
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1 
        elif field.haichi[puyo.puyo2y-1][2]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          return 1
        else:
          return 0
      else:
        return 1


    elif x==21:
      if field.haichi[13][5]!=0 or field.haichi[13][4]!=0:
        return 0
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]!=0: 
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          return 1
        else:
          return 0
      elif field.haichi[puyo.puyo2y][5]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0 and field.haichi[puyo.puyo2y][2]==0:
          return 1
        else:
          return 0
      else:
        return 1 


    elif x==22:
      if field.haichi[13][5]!=0 or field.haichi[13][4]!=0 or field.haichi[13][6]!=0:
        return 0
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]!=0: 
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          return 1
        else:
          return 0
      elif field.haichi[puyo.puyo2y][5]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][2]!=0 and field.haichi[puyo.puyo2y][2]==0:
          return 1
        else:
          return 0
      elif field.haichi[puyo.puyo2y][6]!=0:
        if field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][4]!=0:
          return 1
        elif field.haichi[puyo.puyo2y-1][5]!=0:
          return 1
        else:
          return 0
      else:
        return 1


  def cpu_sousa(self,field,puyo):

    puyo.shita_c=0

    if self.cpu_c==1:
      if field.haichi[13][1]!=0 or field.haichi[13][2]!=0:
        return 0
      if puyo.puyo2x==1:
        if puyo.puyo2y!=puyo.puyo1y-1:
          puyo.kaiten_c=1
        else:
          puyo.shita_c+=self.cpu_os()
          return 1
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x-1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][1]==0 and field.haichi[puyo.puyo2y][2]==0:
        if puyo.puyo2y==puyo.puyo1y+1:
          if field.haichi[puyo.puyo2y-1][puyo.puyo2x+1]==0:
            puyo.kaiten_c=2
          else:
            puyo.kaiten_c=1
        elif puyo.puyo2x==puyo.puyo1x+1:
          puyo.kaiten_c=2
        puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
        if field.haichi[puyo.puyo2y][puyo.puyo2x+1]==0:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif  field.haichi[puyo.puyo2y][2]==0 and field.haichi[puyo.puyo2y-1][2]!=0 :
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y][4]==0:
        if field.haichi[puyo.puyo2y-1][4]!=0: 
          puyo.migi_c+=1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=1
      else: 
        return 0


    elif self.cpu_c==2:
      if field.haichi[13][2]!=0:
        return 0
      if puyo.puyo2x==2:
        if puyo.puyo2y==puyo.puyo1y-1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2x==puyo.puyo1x+1:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x-1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][2]==0:
        if puyo.puyo2y==puyo.puyo1y+1:
          if field.haichi[puyo.puyo2y-1][puyo.puyo2x+1]==0:
            puyo.kaiten_c=2
          else:
            puyo.kaiten_c=1
        elif puyo.puyo2x==puyo.puyo1x+1:
          puyo.kaiten_c=2
        if puyo.puyo2x<2:
          puyo.migi_c+=1
        elif puyo.puyo2x>2:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0: 
        if field.haichi[puyo.puyo2y][puyo.puyo2x+1]==0:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y][4]==0:
        if field.haichi[puyo.puyo2y-1][4]!=0: 
          puyo.migi_c+=1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=1
      else:
        return 0


    elif self.cpu_c==3:
      if field.haichi[11][3]!=0:
        return 0
      if puyo.puyo2x==3:
        if puyo.puyo2y==puyo.puyo1y-1:
          puyo.shita_c+=self.cpu_os()
          return 1
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y][3]==0:
        if puyo.puyo2x<3:
          puyo.migi_c+=1
        elif puyo.puyo2x>3:
          puyo.hidari_c+=1
      else:
        return 0


    elif self.cpu_c==4:
      if field.haichi[13][4]!=0:
        return 0
      if puyo.puyo2x==4:
        if puyo.puyo2y==puyo.puyo1y-1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2x==puyo.puyo1x-1:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]==0:
        if puyo.puyo2y==puyo.puyo1y+1:
          if field.haichi[puyo.puyo2y-1][puyo.puyo2x-1]==0:
            puyo.kaiten_c=1
          else:
            puyo.kaiten_c=2
        elif puyo.puyo2x==puyo.puyo1x-1:
          puyo.kaiten_c=1
        if puyo.puyo2x<4:
          puyo.migi_c+=1
        elif puyo.puyo2x>4:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0: 
        if field.haichi[puyo.puyo2y][puyo.puyo2x-1]==0:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y][2]==0:
        if field.haichi[puyo.puyo2y-1][2]!=0: 
          puyo.hidari_c+=1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=2
      else:
        return 0


    elif self.cpu_c==5:
      if field.haichi[13][5]!=0 or field.haichi[13][4]!=0:
        return 0
      if puyo.puyo2x==5:
        if puyo.puyo2y==puyo.puyo1y-1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2x==puyo.puyo1x-1:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]==0 and field.haichi[puyo.puyo2y][5]==0:
        if puyo.puyo2y==puyo.puyo1y+1:
          if field.haichi[puyo.puyo2y-1][puyo.puyo2x-1]==0:
            puyo.kaiten_c=1
          else:
            puyo.kaiten_c=2
        elif puyo.puyo2x==puyo.puyo1x-1:
          puyo.kaiten_c=1
        if puyo.puyo2x<5:
          puyo.migi_c+=1
        elif puyo.puyo2x>5:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0: 
        if field.haichi[puyo.puyo2y][puyo.puyo2x-1]==0:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y-1][4]!=0 and field.haichi[puyo.puyo2y][4]==0:
        puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y][2]==0:
        if field.haichi[puyo.puyo2y-1][2]!=0: 
          puyo.hidari_c+=1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=2
      else:
        return 0


    elif self.cpu_c==6:
      if field.haichi[13][5]!=0 or field.haichi[13][4]!=0 or field.haichi[13][6]!=0:
        return 0
      if puyo.puyo2x==6:
        if puyo.puyo2y==puyo.puyo1y-1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2x==puyo.puyo1x-1:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]==0 and field.haichi[puyo.puyo2y][5]==0 and field.haichi[puyo.puyo2y][6]==0:
        if puyo.puyo2y==puyo.puyo1y+1:
          if field.haichi[puyo.puyo2y-1][puyo.puyo2x-1]==0:
            puyo.kaiten_c=1
          else:
            puyo.kaiten_c=2
        elif puyo.puyo2x==puyo.puyo1x-1:
          puyo.kaiten_c=1
        puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0: 
        if field.haichi[puyo.puyo2y][puyo.puyo2x-1]==0:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y][4]==0:
        if field.haichi[puyo.puyo2y-1][4]!=0: 
          puyo.migi_c+=1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y][2]==0:
        if field.haichi[puyo.puyo2y-1][2]!=0: 
          puyo.hidari_c+=1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=2
      else:
        return 0


    elif self.cpu_c==7:
      if field.haichi[12][1]!=0 or field.haichi[13][2]!=0:
        return 0
      if puyo.puyo2x==1:
        if puyo.puyo2y!=puyo.puyo1y+1:
          puyo.kaiten_c=2
        else:
          puyo.shita_c+=self.cpu_os()
          return 1
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x-1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][2]==0 and field.haichi[puyo.puyo2y][1]==0:
        if puyo.puyo2y==puyo.puyo1y+1:
          if field.haichi[puyo.puyo2y-1][puyo.puyo2x+1]==0:
            puyo.kaiten_c=2
          else:
            puyo.kaiten_c=1
        elif puyo.puyo2x==puyo.puyo1x+1:
          puyo.kaiten_c=2
        puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
        if field.haichi[puyo.puyo2y][puyo.puyo2x+1]==0:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y-1][2]!=0 and field.haichi[puyo.puyo2y][2]==0:
        puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y][4]==0:
        if field.haichi[puyo.puyo2y-1][4]!=0: 
          puyo.migi_c+=1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=1
      else: 
        return 0


    elif self.cpu_c==8:
      if field.haichi[12][2]!=0:
        return 0
      if puyo.puyo2x==2:
        if puyo.puyo2y==puyo.puyo1y+1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2x==puyo.puyo1x+1:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x-1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][2]==0:
        if puyo.puyo2x>2:
          puyo.hidari_c+=1
        elif puyo.puyo2x<2:
          puyo.migi_c+=1
      else:
        return 0


    elif self.cpu_c==9:
      if field.haichi[11][3]!=0:
        return 0
      if puyo.puyo2x==3:
        if puyo.puyo2y==puyo.puyo1y+1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif field.haichi[puyo.puyo2y][puyo.puyo2x+1]==0:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y][3]==0:
        if puyo.puyo2x>3:
          puyo.hidari_c+=1
        elif puyo.puyo2x<3:
          puyo.migi_c+=1
      else:
        return 0


    elif self.cpu_c==10:
      if field.haichi[12][4]!=0:
        return 0
      if puyo.puyo2x==4:
        if puyo.puyo2y==puyo.puyo1y+1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2x==puyo.puyo1x-1:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]==0:
        if puyo.puyo2x>4:
          puyo.hidari_c+=1
        elif puyo.puyo2x<4:
          puyo.migi_c+=1
      else:
        return 0


    elif self.cpu_c==11:
      if field.haichi[12][5]!=0 or field.haichi[13][4]!=0:
        return 0
      if puyo.puyo2x==5:
        if puyo.puyo2y==puyo.puyo1y+1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2x==puyo.puyo1x-1:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]==0 and field.haichi[puyo.puyo2y][5]==0:
        if puyo.puyo2y==puyo.puyo1y+1:
          if field.haichi[puyo.puyo2y-1][puyo.puyo2x-1]==0:
            puyo.kaiten_c=1
          else:
            puyo.kaiten_c=2
        elif puyo.puyo2x==puyo.puyo1x-1:
          puyo.kaiten_c=1
        if puyo.puyo2x<5:
          puyo.migi_c+=1
        elif puyo.puyo2x>5:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
        if field.haichi[puyo.puyo2y][puyo.puyo2x-1]==0:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y-1][4]!=0 and field.haichi[puyo.puyo2y][4]==0:
        puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y][2]==0:
        if field.haichi[puyo.puyo2y-1][2]!=0: 
          puyo.hidari_c+=1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=2
      else: 
        return 0


    elif self.cpu_c==12:
      if field.haichi[12][6]!=0 or field.haichi[13][5]!=0 or field.haichi[13][4]!=0:
        return 0
      if puyo.puyo2x==6:
        if puyo.puyo2y==puyo.puyo1y+1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2x==puyo.puyo1x-1:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]==0 and field.haichi[puyo.puyo2y][5]==0 and field.haichi[puyo.puyo2y][6]==0:
        if puyo.puyo2y==puyo.puyo1y+1:
          if field.haichi[puyo.puyo2y-1][puyo.puyo2x-1]==0:
            puyo.kaiten_c=1
          else:
            puyo.kaiten_c=2
        elif puyo.puyo2x==puyo.puyo1x-1:
          puyo.kaiten_c=1
        puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
        if field.haichi[puyo.puyo2y][puyo.puyo2x-1]==0:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y][4]==0:
        if field.haichi[puyo.puyo2y-1][4]!=0: 
          puyo.migi_c+=1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y][2]==0:
        if field.haichi[puyo.puyo2y-1][2]!=0: 
          puyo.hidari_c+=1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=2
      else: 
        return 0


    elif self.cpu_c==13:
      if field.haichi[13][1]!=0 or field.haichi[13][2]!=0:
        return 0
      if puyo.puyo2x==1:
        if puyo.puyo2x==puyo.puyo1x-1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2y==puyo.puyo1y+1:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x-1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][1]==0 and field.haichi[puyo.puyo2y][2]==0:
        if puyo.puyo2y==puyo.puyo1y+1:
          if field.haichi[puyo.puyo2y-1][puyo.puyo2x+1]==0:
            puyo.kaiten_c=2
          else:
            puyo.kaiten_c=1
        elif puyo.puyo2x==puyo.puyo1x+1:
          puyo.kaiten_c=2
        puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0:
        if field.haichi[puyo.puyo2y][puyo.puyo2x+1]==0:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y-1][2]!=0 and field.haichi[puyo.puyo2y][2]==0:
        puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y][4]==0:
        if field.haichi[puyo.puyo2y-1][4]!=0: 
          puyo.migi_c+=1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=1
      else: 
        return 0


    elif self.cpu_c==14:
      if field.haichi[13][2]!=0 or field.haichi[11][3]!=0:
        return 0
      if puyo.puyo2x==2:
        if puyo.puyo2x==puyo.puyo1x-1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2y==puyo.puyo1y+1:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x-1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][2]==0:
        if puyo.puyo2y==puyo.puyo1y+1:
          if field.haichi[puyo.puyo2y-1][puyo.puyo2x+1]==0:
            puyo.kaiten_c=2
          else:
            puyo.kaiten_c=1
        elif puyo.puyo2x==puyo.puyo1x+1:
          puyo.kaiten_c=2
        if puyo.puyo2x<2:
          puyo.migi_c+=1
        elif puyo.puyo2x>2:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0: 
        if field.haichi[puyo.puyo2y][puyo.puyo2x+1]==0:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y][4]==0:
        if field.haichi[puyo.puyo2y-1][4]!=0: 
          puyo.migi_c+=1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=1
      else:
        return 0


    elif self.cpu_c==15:
      if field.haichi[11][3]!=0 or field.haichi[13][4]!=0:
        return 0
      if puyo.puyo2x==3 and field.haichi[puyo.puyo2y][4]==0:
        if puyo.puyo2x==puyo.puyo1x-1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2y==puyo.puyo1y+1:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][3]==0 and field.haichi[puyo.puyo2y][4]==0:
        if puyo.puyo2x<3:
          puyo.migi_c+=1
        elif puyo.puyo2x>3:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0: 
        if field.haichi[puyo.puyo2y][puyo.puyo2x+1]==0:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y][2]==0:
        if field.haichi[puyo.puyo2y-1][2]!=0: 
          puyo.hidari_c+=1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=2
      else:
        return 0


    elif self.cpu_c==16:
      if field.haichi[13][4]!=0 or field.haichi[13][5]!=0:
        return 0
      if puyo.puyo2x==4 and field.haichi[puyo.puyo2y][5]==0:
        if puyo.puyo2x==puyo.puyo1x-1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2y==puyo.puyo1y+1:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]==0 and field.haichi[puyo.puyo2y][5]==0:
        if puyo.puyo2y==puyo.puyo1y+1:
          if field.haichi[puyo.puyo2y-1][puyo.puyo2x+1]==0:
            puyo.kaiten_c=2
          else:
            puyo.kaiten_c=1
        elif puyo.puyo2x==puyo.puyo1x+1:
          puyo.kaiten_c=2
        if puyo.puyo2x<4:
          puyo.migi_c+=1
        elif puyo.puyo2x>4:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0: 
        if field.haichi[puyo.puyo2y][puyo.puyo2x+1]==0:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y-1][4]!=0 and field.haichi[puyo.puyo2y][4]==0:
        puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y][2]==0:
        if field.haichi[puyo.puyo2y-1][2]!=0: 
          puyo.hidari_c+=1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=2
      else:
        return 0


    elif self.cpu_c==17:
      if field.haichi[13][5]!=0 or field.haichi[13][4]!=0 or field.haichi[13][6]!=0:
        return 0
      if puyo.puyo2x==5 and field.haichi[puyo.puyo2y][6]==0:
        if puyo.puyo2x==puyo.puyo1x-1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2y==puyo.puyo1y+1:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]==0 and field.haichi[puyo.puyo2y][5]==0 and field.haichi[puyo.puyo2y][6]==0:
        if puyo.puyo2y==puyo.puyo1y+1:
          if field.haichi[puyo.puyo2y-1][puyo.puyo2x+1]==0:
            puyo.kaiten_c=2
          else:
            puyo.kaiten_c=1
        elif puyo.puyo2x==puyo.puyo1x+1:
          puyo.kaiten_c=2
        if puyo.puyo2x<5:
          puyo.migi_c+=1
        elif puyo.puyo2x>5:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0: 
        if field.haichi[puyo.puyo2y][puyo.puyo2x+1]==0:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y][4]==0:
        if field.haichi[puyo.puyo2y-1][4]!=0: 
          puyo.migi_c+=1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y][2]==0:
        if field.haichi[puyo.puyo2y-1][2]!=0: 
          puyo.hidari_c+=1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=2
      else:
        return 0


    elif self.cpu_c==18:
      if field.haichi[13][2]!=0 or field.haichi[13][1]!=0:
        return 0
      if puyo.puyo2x==2 and field.haichi[puyo.puyo2y][1]==0:
        if puyo.puyo2x==puyo.puyo1x+1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2y==puyo.puyo1y+1:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x-1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][2]==0 and field.haichi[puyo.puyo2y][1]==0:
        if puyo.puyo2y==puyo.puyo1y+1:
          if field.haichi[puyo.puyo2y-1][puyo.puyo2x-1]==0:
            puyo.kaiten_c=1
          else:
            puyo.kaiten_c=2
        elif puyo.puyo2x==puyo.puyo1x-1:
          puyo.kaiten_c=1
        if puyo.puyo2x<2:
          puyo.migi_c+=1
        elif puyo.puyo2x>2:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0: 
        if field.haichi[puyo.puyo2y][puyo.puyo2x-1]==0:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y-1][2]!=0 and field.haichi[puyo.puyo2y][2]==0:
        puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y][4]==0:
        if field.haichi[puyo.puyo2y-1][4]!=0: 
          puyo.migi_c+=1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=2
      else:
        return 0


    elif self.cpu_c==19:
      if field.haichi[11][3]!=0 or field.haichi[13][2]!=0:
        return 0
      if puyo.puyo2x==3 and field.haichi[puyo.puyo2y][2]==0:
        if puyo.puyo2x==puyo.puyo1x+1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2y==puyo.puyo1y+1:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x-1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][3]==0 and field.haichi[puyo.puyo2y][2]==0:
        if puyo.puyo2x<3:
          puyo.migi_c+=1
        elif puyo.puyo2x>3:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0: 
        if field.haichi[puyo.puyo2y][puyo.puyo2x-1]==0:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y][4]==0:
        if field.haichi[puyo.puyo2y-1][4]!=0: 
          puyo.migi_c+=1
        elif field.haichi[puyo.puyo2y][5]==0:
          if field.haichi[puyo.puyo2y-1][5]!=0: 
            puyo.migi_c+=1
          elif field.haichi[puyo.puyo2y-1][6]!=0 and field.haichi[puyo.puyo2y][6]==0:
            puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=2
      else:
        return 0


    elif self.cpu_c==20:
      if field.haichi[13][4]!=0 or field.haichi[11][3]!=0:
        return 0
      if puyo.puyo2x==4:
        if puyo.puyo2x==puyo.puyo1x+1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2y==puyo.puyo1y+1:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]==0:
        if puyo.puyo2y==puyo.puyo1y+1:
          if field.haichi[puyo.puyo2y-1][puyo.puyo2x-1]==0:
            puyo.kaiten_c=1
          else:
            puyo.kaiten_c=2
        elif puyo.puyo2x==puyo.puyo1x-1:
          puyo.kaiten_c=1
        if puyo.puyo2x<4:
          puyo.migi_c+=1
        elif puyo.puyo2x>4:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0: 
        if field.haichi[puyo.puyo2y][puyo.puyo2x-1]==0:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y][2]==0:
        if field.haichi[puyo.puyo2y-1][2]!=0: 
          puyo.hidari_c+=1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=2
      else:
        return 0


    elif self.cpu_c==21:
      if field.haichi[13][5]!=0 or field.haichi[13][4]!=0:
        return 0
      if puyo.puyo2x==5:
        if puyo.puyo2x==puyo.puyo1x+1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2y==puyo.puyo1y+1:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]==0 and field.haichi[puyo.puyo2y][5]==0:
        if puyo.puyo2y==puyo.puyo1y+1:
          if field.haichi[puyo.puyo2y-1][puyo.puyo2x-1]==0:
            puyo.kaiten_c=1
          else:
            puyo.kaiten_c=2
        elif puyo.puyo2x==puyo.puyo1x-1:
          puyo.kaiten_c=1
        if puyo.puyo2x<5:
          puyo.migi_c+=1
        elif puyo.puyo2x>5:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0: 
        if field.haichi[puyo.puyo2y][puyo.puyo2x-1]==0:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y-1][4]!=0 and field.haichi[puyo.puyo2y][4]==0:
        puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y][2]==0:
        if field.haichi[puyo.puyo2y-1][2]!=0: 
          puyo.hidari_c+=1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=2
      else:
        return 0


    elif self.cpu_c==22:
      if field.haichi[13][5]!=0 or field.haichi[13][4]!=0 or field.haichi[13][6]!=0:
        return 0
      if puyo.puyo2x==6:
        if puyo.puyo2x==puyo.puyo1x+1:
          puyo.shita_c+=self.cpu_os()
          return 1
        elif puyo.puyo2y==puyo.puyo1y+1:
          puyo.kaiten_c=2
        else:
          puyo.kaiten_c=1
      elif field.haichi[puyo.puyo2y+1][puyo.puyo2x+1]!=0:
        return 0
      elif field.haichi[puyo.puyo2y][4]==0 and field.haichi[puyo.puyo2y][5]==0 and field.haichi[puyo.puyo2y][6]==0:
        if puyo.puyo2y==puyo.puyo1y+1:
          if field.haichi[puyo.puyo2y-1][puyo.puyo2x-1]==0:
            puyo.kaiten_c=1
          else:
            puyo.kaiten_c=2
        elif puyo.puyo2x==puyo.puyo1x-1:
          puyo.kaiten_c=1
        puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y-1][puyo.puyo2x]!=0: 
        if field.haichi[puyo.puyo2y][puyo.puyo2x-1]==0:
          puyo.kaiten_c=1
        else:
          puyo.kaiten_c=2
      elif field.haichi[puyo.puyo2y][4]==0:
        if field.haichi[puyo.puyo2y-1][4]!=0: 
          puyo.migi_c+=1
        elif field.haichi[puyo.puyo2y-1][5]!=0 and field.haichi[puyo.puyo2y][5]==0:
          puyo.migi_c+=1
      elif field.haichi[puyo.puyo2y][2]==0:
        if field.haichi[puyo.puyo2y-1][2]!=0: 
          puyo.hidari_c+=1
        elif field.haichi[puyo.puyo2y-1][1]!=0 and field.haichi[puyo.puyo2y][1]==0:
          puyo.hidari_c+=1
      elif field.haichi[puyo.puyo2y][2]!=0 and field.haichi[puyo.puyo2y][4]!=0:
        puyo.kaiten_c=2
      else:
        return 0
    else:
      return 0

