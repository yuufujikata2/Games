import random

class Tumo():
  def __init__(self):
    self.tumosyote=[random.randint(1,3) for i in range(4)]
    self.fetumosyote=[random.randint(1,3) for i in range(4)]
    while self.fetumosyote[0]==self.fetumosyote[1] and self.fetumosyote[0]==self.fetumosyote[2] and self.fetumosyote[0]==self.fetumosyote[3]:
      self.fetumosyote=[random.randint(1,3) for i in range(4)]
    #self.tumosyote=[1,1,1,1]
    self.tumo=[0 for i in range(256)]
    self.tumo_c=0
    self.tumo_c2=0
    for i in range(256):
      if i<=63:
        self.tumo[i]=1
      elif i<=127:
        self.tumo[i]=2
      elif i<=191:
        self.tumo[i]=3
      else:
        self.tumo[i]=4
    random.shuffle(self.tumo)


