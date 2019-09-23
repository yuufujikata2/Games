import random


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
    self.imapuyo_c=1
    self.hajime_c=1
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
    self.imapuyo_c=0

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
    self.imapuyo_c=0
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

class FEPuyo():
  def __init__(self,tumo):
    self.puyo1x=0
    self.puyo1y=0
    self.puyo1iro=0
    self.puyo2x=0
    self.puyo2y=0
    self.puyo2iro=0
    self.puyo3x=0
    self.puyo3y=0
    self.puyo3iro=0
    self.puyo4x=0
    self.puyo4y=0
    self.puyo4iro=0
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
    self.nexnex=[[0,0,0,0],[0,0,0,0]]
    self.nexnex[0][0]=tumo.fetumosyote[0]
    self.nexnex[0][1]=tumo.fetumosyote[1]
    self.nexnex[1][0]=tumo.fetumosyote[2]
    self.nexnex[1][1]=tumo.fetumosyote[3]
    self.imapuyo_c=1
    self.hajime_c=1
    self.tumoissyuu_c=0
    self.puyosuu_c=0
    self.nexpuyosuu_c=0
    self.nexnexpuyosuu_c=0
    return 

  def syote(self,tumo):
    self.nexnex[0][0]=tumo.fetumosyote[0]
    self.nexnex[0][1]=tumo.fetumosyote[1]
    self.nexnex[1][0]=tumo.fetumosyote[2]
    self.nexnex[1][1]=tumo.fetumosyote[3]
    return 


  def syokika(self,tumo):
    if self.tumoissyuu_c==16:
      self.tumoissyuu_c=1
    else:
      self.tumoissyuu_c+=1
    if self.tumoissyuu_c==1:
      self.puyosuu_c=2
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c+=2
      if tumo.tumo_c>=256:
        tumo.tumo_c=0
    elif self.tumoissyuu_c==2:
      self.puyosuu_c=2
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=3
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      puyo3_c=random.randint(1,2)
      if puyo3_c==1:
        self.nexnex[1][0]=tumo.tumo[tumo.tumo_c]
        self.nexnex[1][1]=tumo.tumo[tumo.tumo_c]
        self.nexnex[1][3]=tumo.tumo[tumo.tumo_c+1]
        self.nexnex[1][2]=0
      else:
        self.nexnex[1][0]=tumo.tumo[tumo.tumo_c+1]
        self.nexnex[1][1]=tumo.tumo[tumo.tumo_c]
        self.nexnex[1][3]=tumo.tumo[tumo.tumo_c]
        self.nexnex[1][2]=0
      tumo.tumo_c+=2
      if tumo.tumo_c>=256:
        tumo.tumo_c=0
    elif self.tumoissyuu_c==3:
      self.puyosuu_c=2
      self.nexpuyosuu_c=3
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c+=2
      if tumo.tumo_c>=256:
        tumo.tumo_c=0
    elif self.tumoissyuu_c==4:
      self.puyosuu_c=3
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo3x=4
      self.puyo3y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][3]
      self.puyo4iro=self.nexnex[0][2]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c+=2
      if tumo.tumo_c>=256:
        tumo.tumo_c=0
    elif self.tumoissyuu_c==5:
      self.puyosuu_c=2
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c+=2
      if tumo.tumo_c>=256:
        tumo.tumo_c=0
    elif self.tumoissyuu_c==6:
      self.puyosuu_c=2
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=5
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][2]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][3]=tumo.tumo[tumo.tumo_c]
      tumo.tumo_c+=1
      if tumo.tumo_c>=256:
        tumo.tumo_c=0
    elif self.tumoissyuu_c==7:
      self.puyosuu_c=2
      self.nexpuyosuu_c=5
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c+=2
      if tumo.tumo_c>=256:
        tumo.tumo_c=0
    elif self.tumoissyuu_c==8:
      self.puyosuu_c=5
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo3x=4
      self.puyo3y=13
      self.puyo4x=4
      self.puyo4y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c+=2
      if tumo.tumo_c>=256:
        tumo.tumo_c=0
    elif self.tumoissyuu_c==9:
      self.puyosuu_c=2
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c+=2
      if tumo.tumo_c>=256:
        tumo.tumo_c=0
    elif self.tumoissyuu_c==10:
      self.puyosuu_c=2
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=4
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][2]=tumo.tumo[tumo.tumo_c+1]
      self.nexnex[1][3]=tumo.tumo[tumo.tumo_c+1]
      if self.nexnex[1][0]==self.nexnex[1][2]:
        if self.nexnex[1][2]==1:
          self.nexnex[1][2]=2
          self.nexnex[1][3]=2
        elif self.nexnex[1][2]==2:
          self.nexnex[1][2]=3
          self.nexnex[1][3]=3
        elif self.nexnex[1][2]==3:
          self.nexnex[1][2]=4
          self.nexnex[1][3]=4
        elif self.nexnex[1][2]==4:
          self.nexnex[1][2]=1
          self.nexnex[1][3]=1
      tumo.tumo_c+=2
      if tumo.tumo_c>=256:
        tumo.tumo_c=0
    elif self.tumoissyuu_c==11:
      self.puyosuu_c=2
      self.nexpuyosuu_c=4
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c+=2
      if tumo.tumo_c>=256:
        tumo.tumo_c=0
    elif self.tumoissyuu_c==12:
      self.puyosuu_c=4
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo3x=4
      self.puyo3y=13
      self.puyo4x=4
      self.puyo4y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c+=2
      if tumo.tumo_c>=256:
        tumo.tumo_c=0
    elif self.tumoissyuu_c==13:
      self.puyosuu_c=2
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c+=2
      if tumo.tumo_c>=256:
        tumo.tumo_c=0
    elif self.tumoissyuu_c==14:
      self.puyosuu_c=2
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=5
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][2]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][3]=tumo.tumo[tumo.tumo_c]
      tumo.tumo_c+=1
      if tumo.tumo_c>=256:
        tumo.tumo_c=0
    elif self.tumoissyuu_c==15:
      self.puyosuu_c=2
      self.nexpuyosuu_c=5
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c+=2
      if tumo.tumo_c>=256:
        tumo.tumo_c=0
    elif self.tumoissyuu_c==16:
      self.puyosuu_c=5
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo3x=4
      self.puyo3y=13
      self.puyo4x=4
      self.puyo4y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c+=2
      if tumo.tumo_c>=256:
        tumo.tumo_c=0
     
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
    self.imapuyo_c=0

    return 

  def syokika2(self,tumo):
    if self.tumoissyuu_c==16:
      self.tumoissyuu_c=1
    else:
      self.tumoissyuu_c+=1
    if self.tumoissyuu_c==1:
      self.puyosuu_c=2
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c2+=2
      if tumo.tumo_c2>=256:
        tumo.tumo_c2=0
    elif self.tumoissyuu_c==2:
      self.puyosuu_c=2
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=3
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      puyo3_c=random.randint(1,2)
      if puyo3_c==1:
        self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2]
        self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2]
        self.nexnex[1][3]=tumo.tumo[tumo.tumo_c2+1]
        self.nexnex[1][2]=0
      else:
        self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2+1]
        self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2]
        self.nexnex[1][3]=tumo.tumo[tumo.tumo_c2]
        self.nexnex[1][2]=0
      tumo.tumo_c2+=2
      if tumo.tumo_c2>=256:
        tumo.tumo_c2=0
    elif self.tumoissyuu_c==3:
      self.puyosuu_c=2
      self.nexpuyosuu_c=3
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c2+=2
      if tumo.tumo_c2>=256:
        tumo.tumo_c2=0
    elif self.tumoissyuu_c==4:
      self.puyosuu_c=3
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo3x=4
      self.puyo3y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][3]
      self.puyo4iro=self.nexnex[0][2]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c2+=2
      if tumo.tumo_c2>=256:
        tumo.tumo_c2=0
    elif self.tumoissyuu_c==5:
      self.puyosuu_c=2
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c2+=2
      if tumo.tumo_c2>=256:
        tumo.tumo_c2=0
    elif self.tumoissyuu_c==6:
      self.puyosuu_c=2
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=5
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][2]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][3]=tumo.tumo[tumo.tumo_c2]
      tumo.tumo_c2+=1
      if tumo.tumo_c2>=256:
        tumo.tumo_c2=0
    elif self.tumoissyuu_c==7:
      self.puyosuu_c=2
      self.nexpuyosuu_c=5
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c2+=2
      if tumo.tumo_c2>=256:
        tumo.tumo_c2=0
    elif self.tumoissyuu_c==8:
      self.puyosuu_c=5
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo3x=4
      self.puyo3y=13
      self.puyo4x=4
      self.puyo4y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c2+=2
      if tumo.tumo_c2>=256:
        tumo.tumo_c2=0
    elif self.tumoissyuu_c==9:
      self.puyosuu_c=2
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c2+=2
      if tumo.tumo_c2>=256:
        tumo.tumo_c2=0
    elif self.tumoissyuu_c==10:
      self.puyosuu_c=2
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=4
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][2]=tumo.tumo[tumo.tumo_c2+1]
      self.nexnex[1][3]=tumo.tumo[tumo.tumo_c2+1]
      if self.nexnex[1][0]==self.nexnex[1][2]:
        if self.nexnex[1][2]==1:
          self.nexnex[1][2]=2
          self.nexnex[1][3]=2
        elif self.nexnex[1][2]==2:
          self.nexnex[1][2]=3
          self.nexnex[1][3]=3
        elif self.nexnex[1][2]==3:
          self.nexnex[1][2]=4
          self.nexnex[1][3]=4
        elif self.nexnex[1][2]==4:
          self.nexnex[1][2]=1
          self.nexnex[1][3]=1
      tumo.tumo_c2+=2
      if tumo.tumo_c2>=256:
        tumo.tumo_c2=0
    elif self.tumoissyuu_c==11:
      self.puyosuu_c=2
      self.nexpuyosuu_c=4
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c2+=2
      if tumo.tumo_c2>=256:
        tumo.tumo_c2=0
    elif self.tumoissyuu_c==12:
      self.puyosuu_c=4
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo3x=4
      self.puyo3y=13
      self.puyo4x=4
      self.puyo4y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c2+=2
      if tumo.tumo_c2>=256:
        tumo.tumo_c2=0
    elif self.tumoissyuu_c==13:
      self.puyosuu_c=2
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c2+=2
      if tumo.tumo_c2>=256:
        tumo.tumo_c2=0
    elif self.tumoissyuu_c==14:
      self.puyosuu_c=2
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=5
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][2]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][3]=tumo.tumo[tumo.tumo_c2]
      tumo.tumo_c2+=1
      if tumo.tumo_c2>=256:
        tumo.tumo_c2=0
    elif self.tumoissyuu_c==15:
      self.puyosuu_c=2
      self.nexpuyosuu_c=5
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c2+=2
      if tumo.tumo_c2>=256:
        tumo.tumo_c2=0
    elif self.tumoissyuu_c==16:
      self.puyosuu_c=5
      self.nexpuyosuu_c=2
      self.nexnexpuyosuu_c=2
      self.puyo1x=3
      self.puyo1y=13
      self.puyo2x=3
      self.puyo2y=12
      self.puyo3x=4
      self.puyo3y=13
      self.puyo4x=4
      self.puyo4y=12
      self.puyo1iro=self.nexnex[0][0]
      self.puyo2iro=self.nexnex[0][1]
      self.puyo3iro=self.nexnex[0][2]
      self.puyo4iro=self.nexnex[0][3]
      self.nexnex[0][0]=self.nexnex[1][0]
      self.nexnex[0][1]=self.nexnex[1][1]
      self.nexnex[0][2]=self.nexnex[1][2]
      self.nexnex[0][3]=self.nexnex[1][3]
      self.nexnex[1][0]=tumo.tumo[tumo.tumo_c2]
      self.nexnex[1][1]=tumo.tumo[tumo.tumo_c2+1]
      self.nexnex[1][2]=0
      self.nexnex[1][3]=0
      tumo.tumo_c2+=2
      if tumo.tumo_c2>=256:
        tumo.tumo_c2=0
     
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
    self.imapuyo_c=0

    return 

  def yokoidou(self,field):
    if self.hidari_c>=10:
      if self.puyosuu_c==2:
        idou=self.idouhantei(field,1)
        if idou==1:
          self.puyo1x-=1
          self.puyo2x-=1
        self.hidari_c=0
      elif self.puyosuu_c==3:
        idou=self.idouhantei(field,31)
        if idou==1:
          self.puyo1x-=1
          self.puyo2x-=1
          self.puyo3x-=1
        self.hidari_c=0
      elif self.puyosuu_c==4 or self.puyosuu_c==5:
        idou=self.idouhantei(field,41)
        if idou==1:
          self.puyo1x-=1
          self.puyo2x-=1
          self.puyo3x-=1
          self.puyo4x-=1
        self.hidari_c=0
    if self.migi_c>=10:
      if self.puyosuu_c==2:
        idou=self.idouhantei(field,2)
        if idou==1:
          self.puyo1x+=1
          self.puyo2x+=1
        self.migi_c=0
      elif self.puyosuu_c==3:
        idou=self.idouhantei(field,32)
        if idou==1:
          self.puyo1x+=1
          self.puyo2x+=1
          self.puyo3x+=1
        self.migi_c=0
      elif self.puyosuu_c==4 or self.puyosuu_c==5:
        idou=self.idouhantei(field,42)
        if idou==1:
          self.puyo1x+=1
          self.puyo2x+=1
          self.puyo3x+=1
          self.puyo4x+=1
        self.migi_c=0
    return 

  def shitaidou(self,field):
    if self.puyosuu_c==2:
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
    elif self.puyosuu_c==3:
      idou=self.idouhantei(field,33)
      if idou==1:
        self.idou_c+=1
        if self.setticount>60:
          self.idou_c+=60
      if idou==0:
        self.setticount+=1
      if self.idou_c>=60:
        self.puyo1y-=1
        self.puyo2y-=1
        self.puyo3y-=1
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
        field.haichi[self.puyo3y][self.puyo3x]=self.puyo3iro
        field.rakka_chigiri(14)
        return 1
    elif self.puyosuu_c==4 or self.puyosuu_c==5:
      idou=self.idouhantei(field,43)
      if idou==1:
        self.idou_c+=1
        if self.setticount>60:
          self.idou_c+=60
      if idou==0:
        self.setticount+=1
      if self.idou_c>=60:
        self.puyo1y-=1
        self.puyo2y-=1
        self.puyo3y-=1
        self.puyo4y-=1
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
        field.haichi[self.puyo3y][self.puyo3x]=self.puyo3iro
        field.haichi[self.puyo4y][self.puyo4x]=self.puyo4iro
        field.rakka_chigiri(14)
        return 1

    return

  def hidarikaiten(self,field):
    if self.puyosuu_c==2:
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
    elif self.puyosuu_c==3:
      self.kaitenhantei(field,31)
    elif self.puyosuu_c==4:
      if self.puyo1x==self.puyo2x and self.puyo1y==self.puyo2y+1:
        self.puyo1y-=1
        self.puyo2x+=1
        self.puyo4y+=1
        self.puyo3x-=1
      elif self.puyo1x==self.puyo2x-1 and self.puyo1y==self.puyo2y:
        self.puyo1x+=1
        self.puyo2y+=1
        self.puyo4x-=1
        self.puyo3y-=1
      elif self.puyo1x==self.puyo2x and self.puyo1y==self.puyo2y-1:
        self.puyo1y+=1
        self.puyo2x-=1
        self.puyo4y-=1
        self.puyo3x+=1
      elif self.puyo1x==self.puyo2x+1 and self.puyo1y==self.puyo2y:
        self.puyo1x-=1
        self.puyo2y-=1
        self.puyo4x+=1
        self.puyo3y+=1
      return
    elif self.puyosuu_c==5:
      if self.puyo1iro==1:
        self.puyo1iro=2
        self.puyo2iro=2
        self.puyo3iro=2
        self.puyo4iro=2
      elif self.puyo1iro==2:
        self.puyo1iro=3
        self.puyo2iro=3
        self.puyo3iro=3
        self.puyo4iro=3
      elif self.puyo1iro==3:
        self.puyo1iro=4
        self.puyo2iro=4
        self.puyo3iro=4
        self.puyo4iro=4
      elif self.puyo1iro==4:
        self.puyo1iro=1
        self.puyo2iro=1
        self.puyo3iro=1
        self.puyo4iro=1
      return

  def migikaiten(self,field):
    if self.puyosuu_c==2:
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
    elif self.puyosuu_c==3:
      self.kaitenhantei(field,32)
    elif self.puyosuu_c==4:
      if self.puyo1x==self.puyo2x and self.puyo1y==self.puyo2y+1:
        self.puyo1x+=1
        self.puyo2y+=1
        self.puyo3y-=1
        self.puyo4x-=1
      elif self.puyo1x==self.puyo2x+1 and self.puyo1y==self.puyo2y:
        self.puyo1y-=1
        self.puyo2x+=1
        self.puyo3x-=1
        self.puyo4y+=1
      elif self.puyo1x==self.puyo2x and self.puyo1y==self.puyo2y-1:
        self.puyo1x-=1
        self.puyo2y-=1
        self.puyo3y+=1
        self.puyo4x+=1
      elif self.puyo1x==self.puyo2x-1 and self.puyo1y==self.puyo2y:
        self.puyo1y+=1
        self.puyo2x-=1
        self.puyo3x+=1
        self.puyo4y-=1
      return
    elif self.puyosuu_c==5:
      if self.puyo1iro==1:
        self.puyo1iro=4
        self.puyo2iro=4
        self.puyo3iro=4
        self.puyo4iro=4
      elif self.puyo1iro==2:
        self.puyo1iro=1
        self.puyo2iro=1
        self.puyo3iro=1
        self.puyo4iro=1
      elif self.puyo1iro==3:
        self.puyo1iro=2
        self.puyo2iro=2
        self.puyo3iro=2
        self.puyo4iro=2
      elif self.puyo1iro==4:
        self.puyo1iro=3
        self.puyo2iro=3
        self.puyo3iro=3
        self.puyo4iro=3
      return
   
  def idouhantei(self,field,x):
    if x==1 and field.haichi[self.puyo1y][self.puyo1x-1]==0 and field.haichi[self.puyo2y][self.puyo2x-1]==0 :
      return 1
    elif x==2 and  field.haichi[self.puyo1y][self.puyo1x+1]==0 and field.haichi[self.puyo2y][self.puyo2x+1]==0:
      return 1
    elif x==3 and  field.haichi[self.puyo1y-1][self.puyo1x]==0 and field.haichi[self.puyo2y-1][self.puyo2x]==0:
      if self.puyosuu_c==2:
        return 1
      elif self.puyosuu_c==3:
        if field.haichi[self.puyo3y-1][self.puyo3x]==0:
          return 1
      elif self.puyosuu_c==4 or self.puyosuu_c==5:
        if field.haichi[self.puyo3y-1][self.puyo3x]==0 and field.haichi[self.puyo4y-1][self.puyo4x]==0:
          return 1
    elif x==31 and field.haichi[self.puyo1y][self.puyo1x-1]==0 and field.haichi[self.puyo2y][self.puyo2x-1]==0 and field.haichi[self.puyo3y][self.puyo3x-1]==0:
      return 1
    elif x==32 and field.haichi[self.puyo1y][self.puyo1x+1]==0 and field.haichi[self.puyo2y][self.puyo2x+1]==0 and field.haichi[self.puyo3y][self.puyo3x+1]==0:
      return 1
    elif x==33 and field.haichi[self.puyo1y-1][self.puyo1x]==0 and field.haichi[self.puyo2y-1][self.puyo2x]==0 and field.haichi[self.puyo3y-1][self.puyo3x]==0:
      return 1
    elif x==41 and field.haichi[self.puyo1y][self.puyo1x-1]==0 and field.haichi[self.puyo2y][self.puyo2x-1]==0 and field.haichi[self.puyo3y][self.puyo3x-1]==0 and field.haichi[self.puyo4y][self.puyo4x-1]==0:
      return 1
    elif x==42 and field.haichi[self.puyo1y][self.puyo1x+1]==0 and field.haichi[self.puyo2y][self.puyo2x+1]==0 and field.haichi[self.puyo3y][self.puyo3x+1]==0 and field.haichi[self.puyo4y][self.puyo4x+1]==0:
      return 1
    elif x==43 and field.haichi[self.puyo1y-1][self.puyo1x]==0 and field.haichi[self.puyo2y-1][self.puyo2x]==0 and field.haichi[self.puyo3y-1][self.puyo3x]==0 and field.haichi[self.puyo4y-1][self.puyo4x]==0:
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
    if x==31:
      if self.puyo1y-1==self.puyo2y:
        if self.puyo3x==self.puyo2x-1:
          if field.haichi[self.puyo2y-1][self.puyo2x]==0:
            self.puyo1y-=1
            self.puyo1x-=1
            self.puyo3x+=1
            self.puyo3y-=1
            return 1
          else:
            self.puyo1x-=1
            self.puyo2y+=1
            self.puyo3x+=1
            return 2
        elif self.puyo3x==self.puyo2x+1:
          if field.haichi[self.puyo2y][self.puyo2x-1]==0:
            self.puyo1y-=1
            self.puyo1x-=1
            self.puyo3x-=1
            self.puyo3y+=1
            return 3
          else:
            self.puyo1y-=1
            self.puyo2x+=1
            self.puyo3y+=1
            return 4
      elif self.puyo1x+1==self.puyo2x:
        if self.puyo3y==self.puyo2y+1:
          if self.puyo1y==13 and field.haichi[self.puyo2y-1][self.puyo2x]!=0:
            return 0
          else:
            if field.haichi[self.puyo2y-1][self.puyo2x]==0:
              self.puyo1y-=1
              self.puyo1x+=1
              self.puyo3x-=1
              self.puyo3y-=1
              return 5
            else:
              self.puyo1x+=1
              self.puyo2y+=1
              self.puyo3x-=1
              return 6
        elif self.puyo3y==self.puyo2y-1:
          if field.haichi[self.puyo2y][self.puyo2x+1]==0:
            self.puyo1y-=1
            self.puyo1x+=1
            self.puyo3x+=1
            self.puyo3y+=1
            return 7
          else:
            self.puyo1y-=1
            self.puyo2x-=1
            self.puyo3y+=1
            return 8
      elif self.puyo1y+1==self.puyo2y:
        if self.puyo3x==self.puyo2x-1:
          if field.haichi[self.puyo2y][self.puyo2x+1]==0:
            self.puyo1y+=1
            self.puyo1x+=1
            self.puyo3x+=1
            self.puyo3y-=1
            return 3
          else:
            self.puyo1y+=1
            self.puyo2x-=1
            self.puyo3y-=1
            return 8
        elif self.puyo3x==self.puyo2x+1:
          self.puyo1y+=1
          self.puyo1x+=1
          self.puyo3y+=1
          self.puyo3x-=1
          return 1
      elif self.puyo1x-1==self.puyo2x:
        if self.puyo3y==self.puyo2y+1:
          if field.haichi[self.puyo2y][self.puyo2x-1]==0:
            self.puyo1y+=1
            self.puyo1x-=1
            self.puyo3y-=1
            self.puyo3x-=1
            return 1
          else:
            self.puyo1y+=1
            self.puyo2x+=1
            self.puyo3y-=1
            return 4
        elif self.puyo3y==self.puyo2y-1:
          self.puyo1y+=1
          self.puyo1x-=1
          self.puyo3y+=1
          self.puyo3x+=1
          return 1
    if x==32:
      if self.puyo1y-1==self.puyo2y:
        if self.puyo3x==self.puyo2x-1:
          if field.haichi[self.puyo2y-1][self.puyo2x]==0:
            self.puyo1y-=1
            self.puyo1x-=1
            self.puyo3x+=1
            self.puyo3y-=1
            return 1
          elif self.puyo2y==13:
            return 0
          else:
            self.puyo1x-=1
            self.puyo2y+=1
            self.puyo3x+=1
            return 1
        elif self.puyo3x==self.puyo2x+1:
          if field.haichi[self.puyo2y][self.puyo2x-1]==0:
            self.puyo1y-=1
            self.puyo1x+=1
            self.puyo3y-=1
            self.puyo3x-=1
            return 1
          else:
            self.puyo1y-=1
            self.puyo2x+=1
            self.puyo3y+=1
            return 1
      elif self.puyo1x-1==self.puyo2x:
        if self.puyo3y==self.puyo2y+1:
          if field.haichi[self.puyo2y-1][self.puyo2x]==0:
            self.puyo1y-=1
            self.puyo1x-=1
            self.puyo3y-=1
            self.puyo3x-=1
            return 1
          elif self.puyo2y==13:
            return 0
          else:
            self.puyo1x-=1
            self.puyo2y+=1
            self.puyo3x+=1
            return 1
        elif self.puyo3y==self.puyo2y-1:
          if field.haichi[self.puyo2y][self.puyo2x-1]==0:
            self.puyo1y-=1
            self.puyo1x-=1
            self.puyo3x-=1
            self.puyo3y+=1
            return 1
          else:
            self.puyo1y-=1
            self.puyo2x+=1
            self.puyo3y+=1
            return 1
      elif self.puyo1y+1==self.puyo2y:
        if self.puyo3x==self.puyo2x-1:
          self.puyo1x-=1
          self.puyo1y+=1
          self.puyo3y+=1
          self.puyo3x+=1
          return 1
        elif self.puyo3x==self.puyo2x+1:
          if field.haichi[self.puyo2y][self.puyo2x-1]==0:
            self.puyo1y+=1
            self.puyo1x-=1
            self.puyo3x-=1
            self.puyo3y-=1
            return 1
          else:
            self.puyo1y+=1
            self.puyo2x+=1
            self.puyo3y-=1
            return 1
      elif self.puyo1x+1==self.puyo2x:
        if self.puyo3y==self.puyo2y+1:
          if field.haichi[self.puyo2y][self.puyo2x+1]==0:
            self.puyo1y+=1
            self.puyo1x+=1
            self.puyo3x+=1
            self.puyo3y-=1
            return 1
          else:
            self.puyo1y+=1
            self.puyo2x-=1
            self.puyo3y-=1
            return 1
        elif self.puyo3y==self.puyo2y-1:
          self.puyo1y+=1
          self.puyo1x+=1
          self.puyo3x-=1
          self.puyo3y+=1
          return 1



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

  def rakka(self,haichi):
    if self.puyo1iro==0 and self.puyo2iro==0:
      return
    while True:
      if haichi[self.puyo1y-1][self.puyo1x]!=0 and haichi[self.puyo2y-1][self.puyo2x]!=0:
        break
      elif haichi[self.puyo1y-1][self.puyo1x]!=0 and self.puyo1x==self.puyo2x and self.puyo1y==self.puyo2y-1:
        break
      elif haichi[self.puyo2y-1][self.puyo2x]!=0 and self.puyo2x==self.puyo1x and self.puyo2y==self.puyo1y-1:
        break
      if haichi[self.puyo1y-1][self.puyo1x]==0:
        self.puyo1y-=1
      if haichi[self.puyo2y-1][self.puyo2x]==0:
        self.puyo2y-=1
    haichi[self.puyo1y][self.puyo1x]=self.puyo1iro
    haichi[self.puyo2y][self.puyo2x]=self.puyo2iro




class AIPuyo_f():
  def __init__(self):
    self.puyo1x=0
    self.puyo1y=0
    self.puyo1iro=0
    self.puyo2x=0
    self.puyo2y=0
    self.puyo2iro=0
    self.puyo3x=0
    self.puyo3y=0
    self.puyo3iro=0
    self.puyo4x=0
    self.puyo4y=0
    self.puyo4iro=0
    self.puyosuu_c=0
    self.nexpuyosuu_c=0
    self.nexnexpuyosuu_c=0
    return

  def syokika(self,puyo):
    self.puyo1x=puyo.puyo1x
    self.puyo1y=puyo.puyo1y
    self.puyo1iro=puyo.puyo1iro
    self.puyo2x=puyo.puyo2x
    self.puyo2y=puyo.puyo2y
    self.puyo2iro=puyo.puyo2iro
    self.puyo3x=puyo.puyo3x
    self.puyo3y=puyo.puyo3y
    self.puyo3iro=puyo.puyo3iro
    self.puyo4x=puyo.puyo4x
    self.puyo4y=puyo.puyo4y
    self.puyo4iro=puyo.puyo4iro
    self.puyosuu_c=puyo.puyosuu_c
    self.nexpuyosuu_c=puyo.nexpuyosuu_c
    self.nexnexpuyosuu_c=puyo.nexnexpuyosuu_c

  def puyooki(self,x):
    if self.puyosuu_c==2:
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
    elif self.puyosuu_c==3:
      if x==1:
        self.puyo1x=1
        self.puyo1y=14
        self.puyo2x=1
        self.puyo2y=13
        self.puyo3x=2
        self.puyo3y=13
      elif x==2:
        self.puyo1x=2
        self.puyo1y=14
        self.puyo2x=2 
        self.puyo2y=13
        self.puyo3x=3 
        self.puyo3y=13
      elif x==3:
        self.puyo1x=3
        self.puyo1y=14
        self.puyo2x=3
        self.puyo2y=13
        self.puyo3x=4
        self.puyo3y=13
      elif x==4:
        self.puyo1x=4
        self.puyo1y=14
        self.puyo2x=4
        self.puyo2y=13
        self.puyo3x=5
        self.puyo3y=13
      elif x==5:
        self.puyo1x=5
        self.puyo1y=14
        self.puyo2x=5
        self.puyo2y=13
        self.puyo3x=6
        self.puyo3y=13
      elif x==6:
        self.puyo1x=2
        self.puyo1y=13
        self.puyo2x=2
        self.puyo2y=14
        self.puyo3x=1
        self.puyo3y=14
      elif x==7:
        self.puyo1x=3
        self.puyo1y=13
        self.puyo2x=3
        self.puyo2y=14
        self.puyo3x=2
        self.puyo3y=14
      elif x==8:
        self.puyo1x=4
        self.puyo1y=13
        self.puyo2x=4
        self.puyo2y=14
        self.puyo3x=3
        self.puyo3y=14
      elif x==9:
        self.puyo1x=5
        self.puyo1y=13
        self.puyo2x=5
        self.puyo2y=14
        self.puyo3x=4
        self.puyo3y=14
      elif x==10:
        self.puyo1x=6
        self.puyo1y=13
        self.puyo2x=6
        self.puyo2y=14
        self.puyo3x=5
        self.puyo3y=14
      elif x==11:
        self.puyo1x=1
        self.puyo1y=13
        self.puyo2x=2
        self.puyo2y=13
        self.puyo3x=2
        self.puyo3y=14
      elif x==12:
        self.puyo1x=2
        self.puyo1y=13
        self.puyo2x=3
        self.puyo2y=13
        self.puyo3x=3
        self.puyo3y=14
      elif x==13:
        self.puyo1x=3
        self.puyo1y=13
        self.puyo2x=4
        self.puyo2y=13
        self.puyo3x=4
        self.puyo3y=14
      elif x==14:
        self.puyo1x=4
        self.puyo1y=13
        self.puyo2x=5
        self.puyo2y=13
        self.puyo3x=5
        self.puyo3y=14
      elif x==15:
        self.puyo1x=5
        self.puyo1y=13
        self.puyo2x=6
        self.puyo2y=13
        self.puyo3x=6
        self.puyo3y=14
      elif x==16:
        self.puyo1x=2
        self.puyo1y=14
        self.puyo2x=1
        self.puyo2y=14
        self.puyo3x=1
        self.puyo3y=13
      elif x==17:
        self.puyo1x=3
        self.puyo1y=14
        self.puyo2x=2
        self.puyo2y=14
        self.puyo3x=2
        self.puyo3y=13
      elif x==18:
        self.puyo1x=4
        self.puyo1y=14
        self.puyo2x=3
        self.puyo2y=14
        self.puyo3x=3
        self.puyo3y=13
      elif x==19:
        self.puyo1x=5
        self.puyo1y=14
        self.puyo2x=4
        self.puyo2y=14
        self.puyo3x=4
        self.puyo3y=13
      elif x==20:
        self.puyo1x=6
        self.puyo1y=14
        self.puyo2x=5
        self.puyo2y=14
        self.puyo3x=5
        self.puyo3y=13
    elif self.puyosuu_c==4:
      if x==1:
        self.puyo1x=1
        self.puyo1y=14
        self.puyo2x=1
        self.puyo2y=13
        self.puyo3x=2
        self.puyo3y=14
        self.puyo4x=2
        self.puyo4y=13
      elif x==2:
        self.puyo1x=2
        self.puyo1y=14
        self.puyo2x=2 
        self.puyo2y=13
        self.puyo3x=3 
        self.puyo3y=14
        self.puyo4x=3 
        self.puyo4y=13
      elif x==3:
        self.puyo1x=3
        self.puyo1y=14
        self.puyo2x=3
        self.puyo2y=13
        self.puyo3x=4
        self.puyo3y=14
        self.puyo4x=4
        self.puyo4y=13
      elif x==4:
        self.puyo1x=4
        self.puyo1y=14
        self.puyo2x=4
        self.puyo2y=13
        self.puyo3x=5
        self.puyo3y=14
        self.puyo4x=5
        self.puyo4y=13
      elif x==5:
        self.puyo1x=5
        self.puyo1y=14
        self.puyo2x=5
        self.puyo2y=13
        self.puyo3x=6
        self.puyo3y=14
        self.puyo4x=6
        self.puyo4y=13
      elif x==6:
        self.puyo1x=2
        self.puyo1y=13
        self.puyo2x=2
        self.puyo2y=14
        self.puyo3x=1
        self.puyo3y=13
        self.puyo4x=1
        self.puyo4y=14
      elif x==7:
        self.puyo1x=3
        self.puyo1y=13
        self.puyo2x=3
        self.puyo2y=14
        self.puyo3x=2
        self.puyo3y=13
        self.puyo4x=2
        self.puyo4y=14
      elif x==8:
        self.puyo1x=4
        self.puyo1y=13
        self.puyo2x=4
        self.puyo2y=14
        self.puyo3x=3
        self.puyo3y=13
        self.puyo4x=3
        self.puyo4y=14
      elif x==9:
        self.puyo1x=5
        self.puyo1y=13
        self.puyo2x=5
        self.puyo2y=14
        self.puyo3x=4
        self.puyo3y=13
        self.puyo4x=4
        self.puyo4y=14
      elif x==10:
        self.puyo1x=6
        self.puyo1y=13
        self.puyo2x=6
        self.puyo2y=14
        self.puyo3x=5
        self.puyo3y=13
        self.puyo4x=5
        self.puyo4y=14
      elif x==11:
        self.puyo1x=1
        self.puyo1y=13
        self.puyo2x=2
        self.puyo2y=13
        self.puyo3x=1
        self.puyo3y=14
        self.puyo4x=2
        self.puyo4y=14
      elif x==12:
        self.puyo1x=2
        self.puyo1y=13
        self.puyo2x=3
        self.puyo2y=13
        self.puyo3x=2
        self.puyo3y=14
        self.puyo4x=3
        self.puyo4y=14
      elif x==13:
        self.puyo1x=3
        self.puyo1y=13
        self.puyo2x=4
        self.puyo2y=13
        self.puyo3x=3
        self.puyo3y=14
        self.puyo4x=4
        self.puyo4y=14
      elif x==14:
        self.puyo1x=4
        self.puyo1y=13
        self.puyo2x=5
        self.puyo2y=13
        self.puyo3x=4
        self.puyo3y=14
        self.puyo4x=5
        self.puyo4y=14
      elif x==15:
        self.puyo1x=5
        self.puyo1y=13
        self.puyo2x=6
        self.puyo2y=13
        self.puyo3x=5
        self.puyo3y=14
        self.puyo4x=6
        self.puyo4y=14
      elif x==16:
        self.puyo1x=2
        self.puyo1y=14
        self.puyo2x=1
        self.puyo2y=14
        self.puyo3x=1
        self.puyo3y=13
      elif x==17:
        self.puyo1x=3
        self.puyo1y=14
        self.puyo2x=2
        self.puyo2y=14
        self.puyo3x=2
        self.puyo3y=13
      elif x==18:
        self.puyo1x=4
        self.puyo1y=14
        self.puyo2x=3
        self.puyo2y=14
        self.puyo3x=3
        self.puyo3y=13
      elif x==19:
        self.puyo1x=5
        self.puyo1y=14
        self.puyo2x=4
        self.puyo2y=14
        self.puyo3x=4
        self.puyo3y=13
      elif x==20:
        self.puyo1x=6
        self.puyo1y=14
        self.puyo2x=5
        self.puyo2y=14
        self.puyo3x=5
        self.puyo3y=13
    elif self.puyosuu_c==4:
      if x==1:
        self.puyo1iro=1
        self.puyo2iro=1
        self.puyo3iro=1
        self.puyo4iro=1
        self.puyo1x=1
        self.puyo1y=14
        self.puyo2x=1
        self.puyo2y=13
        self.puyo3x=2
        self.puyo3y=14
        self.puyo4x=2
        self.puyo4y=13
      elif x==2:
        self.puyo1iro=1
        self.puyo2iro=1
        self.puyo3iro=1
        self.puyo4iro=1
        self.puyo1x=2
        self.puyo1y=14
        self.puyo2x=2 
        self.puyo2y=13
        self.puyo3x=3 
        self.puyo3y=14
        self.puyo4x=3 
        self.puyo4y=13
      elif x==3:
        self.puyo1iro=1
        self.puyo2iro=1
        self.puyo3iro=1
        self.puyo4iro=1
        self.puyo1x=3
        self.puyo1y=14
        self.puyo2x=3
        self.puyo2y=13
        self.puyo3x=4
        self.puyo3y=14
        self.puyo4x=4
        self.puyo4y=13
      elif x==4:
        self.puyo1iro=1
        self.puyo2iro=1
        self.puyo3iro=1
        self.puyo4iro=1
        self.puyo1x=4
        self.puyo1y=14
        self.puyo2x=4
        self.puyo2y=13
        self.puyo3x=5
        self.puyo3y=14
        self.puyo4x=5
        self.puyo4y=13
      elif x==5:
        self.puyo1iro=1
        self.puyo2iro=1
        self.puyo3iro=1
        self.puyo4iro=1
        self.puyo1x=5
        self.puyo1y=14
        self.puyo2x=5
        self.puyo2y=13
        self.puyo3x=6
        self.puyo3y=14
        self.puyo4x=6
        self.puyo4y=13
      elif x==6:
        self.puyo1iro=2
        self.puyo2iro=2
        self.puyo3iro=2
        self.puyo4iro=2
        self.puyo1x=1
        self.puyo1y=14
        self.puyo2x=1
        self.puyo2y=13
        self.puyo3x=2
        self.puyo3y=14
        self.puyo4x=2
        self.puyo4y=13
      elif x==7:
        self.puyo1iro=2
        self.puyo2iro=2
        self.puyo3iro=2
        self.puyo4iro=2 
        self.puyo1x=2
        self.puyo1y=14
        self.puyo2x=2 
        self.puyo2y=13
        self.puyo3x=3 
        self.puyo3y=14
        self.puyo4x=3 
        self.puyo4y=13
      elif x==8:
        self.puyo1iro=2
        self.puyo2iro=2
        self.puyo3iro=2
        self.puyo4iro=2
        self.puyo1x=3
        self.puyo1y=14
        self.puyo2x=3
        self.puyo2y=13
        self.puyo3x=4
        self.puyo3y=14
        self.puyo4x=4
        self.puyo4y=13
      elif x==9:
        self.puyo1iro=2
        self.puyo2iro=2
        self.puyo3iro=2
        self.puyo4iro=2
        self.puyo1x=4
        self.puyo1y=14
        self.puyo2x=4
        self.puyo2y=13
        self.puyo3x=5
        self.puyo3y=14
        self.puyo4x=5
        self.puyo4y=13
      elif x==10:
        self.puyo1iro=2
        self.puyo2iro=2
        self.puyo3iro=2
        self.puyo4iro=2
        self.puyo1x=5
        self.puyo1y=14
        self.puyo2x=5
        self.puyo2y=13
        self.puyo3x=6
        self.puyo3y=14
        self.puyo4x=6
        self.puyo4y=13
      elif x==11:
        self.puyo1iro=3
        self.puyo2iro=3
        self.puyo3iro=3
        self.puyo4iro=3
        self.puyo1x=1
        self.puyo1y=14
        self.puyo2x=1
        self.puyo2y=13
        self.puyo3x=2
        self.puyo3y=14
        self.puyo4x=2
        self.puyo4y=13
      elif x==12:
        self.puyo1iro=3
        self.puyo2iro=3
        self.puyo3iro=3
        self.puyo4iro=3 
        self.puyo1x=2
        self.puyo1y=14
        self.puyo2x=2 
        self.puyo2y=13
        self.puyo3x=3 
        self.puyo3y=14
        self.puyo4x=3 
        self.puyo4y=13
      elif x==13:
        self.puyo1iro=3
        self.puyo2iro=3
        self.puyo3iro=3
        self.puyo4iro=3
        self.puyo1x=3
        self.puyo1y=14
        self.puyo2x=3
        self.puyo2y=13
        self.puyo3x=4
        self.puyo3y=14
        self.puyo4x=4
        self.puyo4y=13
      elif x==14:
        self.puyo1iro=3
        self.puyo2iro=3
        self.puyo3iro=3
        self.puyo4iro=3
        self.puyo1x=4
        self.puyo1y=14
        self.puyo2x=4
        self.puyo2y=13
        self.puyo3x=5
        self.puyo3y=14
        self.puyo4x=5
        self.puyo4y=13
      elif x==15:
        self.puyo1iro=3
        self.puyo2iro=3
        self.puyo3iro=3
        self.puyo4iro=3
        self.puyo1x=5
        self.puyo1y=14
        self.puyo2x=5
        self.puyo2y=13
        self.puyo3x=6
        self.puyo3y=14
        self.puyo4x=6
        self.puyo4y=13
      elif x==16:
        self.puyo1iro=4
        self.puyo2iro=4
        self.puyo3iro=4
        self.puyo4iro=4
        self.puyo1x=1
        self.puyo1y=14
        self.puyo2x=1
        self.puyo2y=13
        self.puyo3x=2
        self.puyo3y=14
        self.puyo4x=2
        self.puyo4y=13
      elif x==17:
        self.puyo1iro=4
        self.puyo2iro=4
        self.puyo3iro=4
        self.puyo4iro=4 
        self.puyo1x=2
        self.puyo1y=14
        self.puyo2x=2 
        self.puyo2y=13
        self.puyo3x=3 
        self.puyo3y=14
        self.puyo4x=3 
        self.puyo4y=13
      elif x==18:
        self.puyo1iro=4
        self.puyo2iro=4
        self.puyo3iro=4
        self.puyo4iro=4
        self.puyo1x=3
        self.puyo1y=14
        self.puyo2x=3
        self.puyo2y=13
        self.puyo3x=4
        self.puyo3y=14
        self.puyo4x=4
        self.puyo4y=13
      elif x==19:
        self.puyo1iro=4
        self.puyo2iro=4
        self.puyo3iro=4
        self.puyo4iro=4
        self.puyo1x=4
        self.puyo1y=14
        self.puyo2x=4
        self.puyo2y=13
        self.puyo3x=5
        self.puyo3y=14
        self.puyo4x=5
        self.puyo4y=13
      elif x==20:
        self.puyo1iro=4
        self.puyo2iro=4
        self.puyo3iro=4
        self.puyo4iro=4
        self.puyo1x=5
        self.puyo1y=14
        self.puyo2x=5
        self.puyo2y=13
        self.puyo3x=6
        self.puyo3y=14
        self.puyo4x=6
        self.puyo4y=13


    return

  def rakka(self,haichi):
    if self.puyo1iro==0 and self.puyo2iro==0:
      return
    while True:
      if haichi[self.puyo1y-1][self.puyo1x]!=0 and haichi[self.puyo2y-1][self.puyo2x]!=0:
        break
      elif haichi[self.puyo1y-1][self.puyo1x]!=0 and self.puyo1x==self.puyo2x and self.puyo1y==self.puyo2y-1:
        break
      elif haichi[self.puyo2y-1][self.puyo2x]!=0 and self.puyo2x==self.puyo1x and self.puyo2y==self.puyo1y-1:
        break
      if haichi[self.puyo1y-1][self.puyo1x]==0:
        self.puyo1y-=1
      if haichi[self.puyo2y-1][self.puyo2x]==0:
        self.puyo2y-=1
    haichi[self.puyo1y][self.puyo1x]=self.puyo1iro
    haichi[self.puyo2y][self.puyo2x]=self.puyo2iro

