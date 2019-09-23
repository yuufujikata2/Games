import ctypes
import numpy as np
import time
import aiclass 
from cProfile import Profile
import threading
class Fort():
  def __init__(self):
    self.f=ctypes.CDLL("./libfortfield.so")
    self.f.rensashirabe.argtypes=[np.ctypeslib.ndpointer(dtype=np.int32)]
    self.f.rensashirabe.restype=ctypes.c_int

  def call_fortran(self,A):
    B=np.array(A,dtype=np.int32)
    BT=B.flatten("F")
    a=self.f.rensashirabe(BT)
    return a


class Forttest(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    haichi=[[0 for i in range(8)] for j in range(15)]
    for i in range(15):
      haichi[i][0]=20
      haichi[i][7]=20
    for i in range(1,7):
      haichi[0][i]=20
    fort=Fort()
    ai=aiclass.AIField(haichi)
    t1=time.time()
    pr=Profile()
    pr.enable()
    for i in range(1000):
      ai.haichi[1][1]=i%4
      ai.haichi[1][2]=i%3
      ai.haichi[1][3]=i%2
      ai.haichi[1][4]=i%3
      ai.haichi[1][5]=4
      ai.haichi[1][6]=1
      ai.haichi[2][1]=1
      ai.haichi[2][2]=1
      ai.haichi[2][3]=3
      ai.haichi[2][4]=2
      ai.haichi[2][5]=3
      
      fort.call_fortran(ai.haichi)
    pr.disable()
    pr.print_stats()
    t2=time.time()
    print(t2-t1)
    print(haichi)
   


def main():
  fort=Forttest()
  fort.start()


if __name__=="__main__":
  main()
