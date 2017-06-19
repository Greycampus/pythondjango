from threading import Thread
import sys
from colors import *
i = 1
j = 1
k = 1
def runA():
        global i
        while(i<=k):
                sys.stdout.write(GREEN)
                print(str(int(2*i))+'\n')
                i+=1

def runB():
        global j
        while(j<=k):
                sys.stdout.write(CYAN)
                print(str(int(3*j))+'\n')
                j+=1

if __name__ == "__main__":
        k = int(input('enter the nth term:'))
        t1 = Thread(target = runA)
        t2 = Thread(target = runB)
        t1.setDaemon(True)
        t2.setDaemon(True)
        t1.start()
        t2.start()
        while i<=k and j<=k:
                pass
