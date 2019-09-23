


class Puyo():
  def __init__(self,tumo):
    self.puyo1x=0
    self.puyo1y=0
    self.puyo1iro=0
    self.puyo2x=0
    self.puyo2y=0
    self.puyo2iro=0
    self.hidari_c=0
    self.migi_c=0
    self.shita_c=0
    self.kaiten_c=0
    self.setticount=0
    self.idoucount=0
    self.surinukecount=0
    self.surinukecount2=0
    self.suri=-11
    self.suri2=-11
    self.rakkab_c=0
    self.nexnex=[0,0,0,0]
    self.n1=0
    self.n2=0
    self.n3=0
    self.n4=0
    self.n1=tumo.tumosyote[0]
    self.n2=tumo.tumosyote[1]
    self.n3=tumo.tumosyote[2]
    self.n4=tumo.tumosyote[3]
    return 

  def syote(self,tumo):
    self.n1=tumo.tumosyote[0]
    self.n2=tumo.tumosyote[1]
    self.n3=tumo.tumosyote[2]
    self.n4=tumo.tumosyote[3]
    self.nexnex[0]=self.n1
    self.nexnex[1]=self.n2
    self.nexnex[2]=self.n3
    self.nexnex[3]=self.n4
    return 

  def syokika(self,tumo):
    self.puyo1x=3
    self.puyo1y=13
    self.puyo2x=3
    self.puyo2y=12
    self.puyo1iro=self.n1
    self.puyo2iro=self.n2
    self.n1=self.n3
    self.n2=self.n4
    self.n3=tumo.tumo[tumo.tumo_c]
    self.n4=tumo.tumo[tumo.tumo_c+1]
    tumo.tumo_c+=2
    if tumo.tumo_c==256:
      tumo.tumo_c=0
    self.nexnex[0]=self.n1
    self.nexnex[1]=self.n2
    self.nexnex[2]=self.n3
    self.nexnex[3]=self.n4
    self.hidari_c=0
    self.migi_c=0
    self.shita_c=0
    self.kaiten_c=0
    self.idou_c=0
    self.setticount=0
    self.surinukecount=0
    self.surinukecount2=0
    self.suri=-11
    self.suri2=-11
    self.rakkab_c=0
    return 

  def syokika2(self,tumo):
    self.puyo1x=3
    self.puyo1y=13
    self.puyo2x=3
    self.puyo2y=12
    self.puyo1iro=self.n1
    self.puyo2iro=self.n2
    self.n1=self.n3
    self.n2=self.n4
    self.n3=tumo.tumo[tumo.tumo_c2]
    self.n4=tumo.tumo[tumo.tumo_c2+1]
    tumo.tumo_c2+=2
    if tumo.tumo_c2==256:
      tumo.tumo_c2=0
    self.nexnex[0]=self.n1
    self.nexnex[1]=self.n2
    self.nexnex[2]=self.n3
    self.nexnex[3]=self.n4
    self.hidari_c=0
    self.migi_c=0
    self.shita_c=0
    self.kaiten_c=0
    self.idou_c=0
    self.setticount=0
    self.surinukecount=0
    self.surinukecount2=0
    self.suri=-11
    self.suri2=-11
    self.rakkab_c=0
    return 


  def yokoidou(self,field):
    if self.hidari_c>=10:
      idou=self.idouhantei(field,1)
      if idou==1:
        self.puyo1x-=1
        self.puyo2x-=1
      self.hidari_c=0
    if self.migi_c>=10:
      idou=self.idouhantei(field,2)
      if idou==1:
        self.puyo1x+=1
        self.puyo2x+=1
      self.migi_c=0
    return 

  def shitaidou(self,field):
    idou=self.idouhantei(field,3)
    if idou==1:
      self.idou_c+=1
      if self.setticount>60:
        self.idou_c+=60
    if idou==0:
      self.setticount+=1
    if self.idou_c>=60:
      self.puyo1y-=1
      self.puyo2y-=1
      self.idou_c=0
      self.setticount=0
      if self.rakkab_c!=0:
        field.counttotal_r+=1
        field.counttotal2+=1
        self.rakkab_c=0
    if self.setticount>=60:
      field.haichi_c=0
      field.haichi[self.puyo1y][self.puyo1x]=self.puyo1iro
      field.haichi[self.puyo2y][self.puyo2x]=self.puyo2iro
      field.rakka_chigiri(14)
      return 1
    return

  def hidarikaiten(self,field):
    kaiten=self.kaitenhantei(field,1)
    if kaiten==1:
      self.puyo1x-=1
      self.puyo1y-=1
    elif kaiten==2:
      self.puyo1x+=1
      self.puyo1y-=1
    elif kaiten==3:
      self.puyo1x+=1
      self.puyo1y+=1
    elif kaiten==4:
      self.puyo1x-=1
      self.puyo1y+=1
    elif kaiten==5:
      self.puyo1y-=1
      self.puyo2x+=1
    elif kaiten==6:
      self.puyo1y+=1
      self.puyo2x-=1
    elif kaiten==7:
      if self.surinukecount-self.suri<30:
        self.puyo1y-=1
        self.puyo2y+=1
      self.suri=self.surinukecount
    elif kaiten==8:
      if self.surinukecount2-self.suri2<30:
        self.puyo1y+=1
        self.puyo2y-=1
      self.suri2=self.surinukecount
    elif kaiten==10:
      self.puyo1x+=1
      self.puyo2y+=1
    return

  def migikaiten(self,field):
    kaiten=self.kaitenhantei(field,2)
    if kaiten==1:
      self.puyo1x+=1
      self.puyo1y-=1
    elif kaiten==2:
      self.puyo1x-=1
      self.puyo1y-=1
    elif kaiten==3:
      self.puyo1x-=1
      self.puyo1y+=1
    elif kaiten==4:
      self.puyo1x+=1
      self.puyo1y+=1
    elif kaiten==5:
      self.puyo1y-=1
      self.puyo2x-=1
    elif kaiten==6:
      self.puyo1y+=1
      self.puyo2x+=1
    elif kaiten==7:
      if self.surinukecount-self.suri<30:
        self.puyo1y-=1
        self.puyo2y+=1
      self.suri=self.surinukecount
    elif kaiten==8:
      if self.surinukecount2-self.suri2<30:
        self.puyo1y+=1
        self.puyo2y-=1
      self.suri2=self.surinukecount2
    elif kaiten==10:
      self.puyo1x-=1
      self.puyo2y+=1
    return

  def idouhantei(self,field,x):
    if x==1 and field.haichi[self.puyo1y][self.puyo1x-1]==0 and field.haichi[self.puyo2y][self.puyo2x-1]==0 :
      return 1
    elif x==2 and  field.haichi[self.puyo1y][self.puyo1x+1]==0 and field.haichi[self.puyo2y][self.puyo2x+1]==0:
      return 1
    elif x==3 and  field.haichi[self.puyo1y-1][self.puyo1x]==0 and field.haichi[self.puyo2y-1][self.puyo2x]==0:
      return 1
    return 0

  def kaitenhantei(self,field,x):
    if x==1:
      if self.puyo1y-1==self.puyo2y:
        if field.haichi[self.puyo2y][self.puyo2x-1]==0:
          return 1
        elif field.haichi[self.puyo2y][self.puyo2x+1]==0:
          return 5
        else:
          return 7
      elif self.puyo1x+1==self.puyo2x:
        if self.puyo1y==13 and field.haichi[self.puyo2y-1][self.puyo2x]!=0:
          return 0
        else:
          if field.haichi[self.puyo2y-1][self.puyo2x]==0:
            return 2
          else:
            return 10
      elif self.puyo1y+1==self.puyo2y:
        if field.haichi[self.puyo2y][self.puyo2x+1]==0:
          return 3
        elif field.haichi[self.puyo2y][self.puyo2x-1]==0:
          return 6
        else:
          return 8
      elif self.puyo1x-1==self.puyo2x:
        return 4
    if x==2:
      if self.puyo1y-1==self.puyo2y:
        if field.haichi[self.puyo2y][self.puyo2x+1]==0:
          return 1
        elif field.haichi[self.puyo2y][self.puyo2x-1]==0:
          return 5
        else:
          return 7
      elif self.puyo1x-1==self.puyo2x:
        if  field.haichi[self.puyo2y-1][self.puyo2x]!=0 and self.puyo1y==13:
          return 0
        else:
          if field.haichi[self.puyo2y-1][self.puyo2x]==0:
            return 2
          else:
            return 10
      elif self.puyo1y+1==self.puyo2y:
        if field.haichi[self.puyo2y][self.puyo2x-1]==0:
          return 3
        elif field.haichi[self.puyo2y][self.puyo2x+1]==0:
          return 6
        else:
          return 8
      elif self.puyo1x+1==self.puyo2x:
        return 4
    return 0

class AIPuyo():
  def __init__(self):
    self.puyo1x=0
    self.puyo1y=0
    self.puyo1iro=0
    self.puyo2x=0
    self.puyo2y=0
    self.puyo2iro=0
    return
  def syokika(self,puyo):
    self.puyo1x=puyo.puyo1x
    self.puyo1y=puyo.puyo1y
    self.puyo1iro=puyo.puyo1iro
    self.puyo2x=puyo.puyo2x
    self.puyo2y=puyo.puyo2y
    self.puyo2iro=puyo.puyo2iro

  def puyooki(self,x):
    if x==1:
      self.puyo1x=1
      self.puyo1y=14
      self.puyo2x=1
      self.puyo2y=13
    elif x==2:
      self.puyo1x=2
      self.puyo1y=14
      self.puyo2x=2 
      self.puyo2y=13
    elif x==3:
      self.puyo1x=3
      self.puyo1y=14
      self.puyo2x=3
      self.puyo2y=13
    elif x==4:
      self.puyo1x=4
      self.puyo1y=14
      self.puyo2x=4
      self.puyo2y=13
    elif x==5:
      self.puyo1x=5
      self.puyo1y=14
      self.puyo2x=5
      self.puyo2y=13
    elif x==6:
      self.puyo1x=6
      self.puyo1y=14
      self.puyo2x=6
      self.puyo2y=13
    elif x==7:
      self.puyo1x=1
      self.puyo1y=13
      self.puyo2x=1
      self.puyo2y=14
    elif x==8:
      self.puyo1x=2
      self.puyo1y=13
      self.puyo2x=2
      self.puyo2y=14
    elif x==9:
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=14
    elif x==10:
      self.puyo1x=4
      self.puyo1y=13
      self.puyo2x=4
      self.puyo2y=14
    elif x==11:
      self.puyo1x=5
      self.puyo1y=13
      self.puyo2x=5
      self.puyo2y=14
    elif x==12:
      self.puyo1x=6
      self.puyo1y=13
      self.puyo2x=6
      self.puyo2y=14
    elif x==13:
      self.puyo1x=2
      self.puyo1y=13
      self.puyo2x=1
      self.puyo2y=13
    elif x==14:
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=2
      self.puyo2y=13
    elif x==15:
      self.puyo1x=4
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=13
    elif x==16:
      self.puyo1x=5
      self.puyo1y=13
      self.puyo2x=4
      self.puyo2y=13
    elif x==17:
      self.puyo1x=6
      self.puyo1y=13
      self.puyo2x=5
      self.puyo2y=13
    elif x==18:
      self.puyo1x=1
      self.puyo1y=13
      self.puyo2x=2
      self.puyo2y=13
    elif x==19:
      self.puyo1x=2
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=13
    elif x==20:
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=4
      self.puyo2y=13
    elif x==21:
      self.puyo1x=4
      self.puyo1y=13
      self.puyo2x=5
      self.puyo2y=13
    elif x==22:
      self.puyo1x=5
      self.puyo1y=13
      self.puyo2x=6
      self.puyo2y=13
    return

  def rakka(self,field):
    while True:
      if field.haichi[self.puyo1y-1][self.puyo1x]!=0 and field.haichi[self.puyo2y-1][self.puyo2x]!=0:
        break
      elif field.haichi[self.puyo1y-1][self.puyo1x]!=0 and self.puyo1x==self.puyo2x and self.puyo1y==self.puyo2y-1:
        break
      elif field.haichi[self.puyo2y-1][self.puyo2x]!=0 and self.puyo2x==self.puyo1x and self.puyo2y==self.puyo1y-1:
        break
      if field.haichi[self.puyo1y-1][self.puyo1x]==0:
        self.puyo1y-=1
      if field.haichi[self.puyo2y-1][self.puyo2x]==0:
        self.puyo2y-=1
    field.haichi[self.puyo1y][self.puyo1x]=self.puyo1iro
    field.haichi[self.puyo2y][self.puyo2x]=self.puyo2iro

