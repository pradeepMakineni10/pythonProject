#multi threading is a process which runs parallely multiple methods at the same time can be considered as multi threading.
#there is a run method in Thread class, actually we need to use run method
from time import *
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()


t1.start()
sleep(0.2)
t2.start()

t1.join() #wait for the t1 class to be execute
t2.join() #wait for the t2 class to be execute

print('bye')