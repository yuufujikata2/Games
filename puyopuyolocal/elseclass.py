import pygame
from pygame.locals import *

class Event():
  def __init__(self):
    self.souevent=[]
    return

  def tuika(self):
    self.souevent.extend(pygame.event.get())
    return

  def sakujo(self,x,y):
    self.souevent=[i for i in self.souevent if i.type==QUIT or (i.type==KEYDOWN and (i.key==x or i.key==y))]
    return

class Syuuryou():
  def __init__(self):
    self.syuuryou_c=1 
    return

