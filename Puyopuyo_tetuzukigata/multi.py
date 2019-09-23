import threading,time
'''
def prints(name,sleep_time):
  for i in range(10):
    print(name+':'+str(i))
    time.sleep(sleep_time)

thread1=threading.Thread(target=prints,args=('A',1,))
thread2=threading.Thread(target=prints,args=('B',1,))

thread1.start()
thread1.join()
thread2.start()
'''
'''
class MyThread(threading.Thread):
  def __init__(self,count):
    threading.Thread.__init__(self)
    self.count=count
    self.return_value=None

  def run(self):
    sum_value=0
    for i in range(1,1+self.count):
      sum_value+=i
      time.sleep(0.1)
    self.return_value=sum_value

  def get_value(self):
    return self.return_value
thread1=MyThread(5)
thread2=MyThread(10)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(thread1.return_value)
print(thread1.get_value())
print(thread2.return_value)
print(thread2.get_value())
'''
global_counter=5
global_lock=threading.Lock()
class MyThread(threading.Thread):
  def __init__(self,name,sleep_time):
    threading.Thread.__init__(self)
    self.name=name
    self.sleep_time=sleep_time

  def run(self):
    global global_counter
    global global_lock

    global_lock.acquire()

    count=global_counter
    print(self.name+': read global_value '+str(global_counter))

    print(self.name +': do something')
    time.sleep(self.sleep_time)

    global_counter=count-1
    print(self.name+': write global_value '+str(global_counter))

    global_lock.release()

thread1=MyThread('A',5)
thread2=MyThread('B',3)
thread1.start()
time.sleep(1)
thread2.start()

thread1.join()
thread2.join()

print('result; '+str(global_counter))

