#importing the threads from threading module
from threading import Thread
import sys
#colors is not python library its defined in colors.py file don't forget to include the file in same directory of execution
from colors import *
i = 1
j = 1
k = 1
def runA():
        global i
        while(i<=k):
                #converting output to green in terminal only works in linux
                sys.stdout.write(GREEN)
                #print 2 multiple
                print(str(int(2*i))+'\n')
                i+=1

def runB():
        global j
        while(j<=k):
            #converting output to cyan only works in linux
                sys.stdout.write(CYAN)
                #print 3 multiple
                print(str(int(3*j))+'\n')
                j+=1

if __name__ == "__main__":
        k = int(input('enter the nth term:'))
        #set target fot thread1
        t1 = Thread(target = runA)
        #set target for thread2
        t2 = Thread(target = runB)
        #starting daemon for threads
        t1.setDaemon(True)
        t2.setDaemon(True)
        #starting threads
        t1.start()
        t2.start()
        #while for running of threads
        while i<=k and j<=k:
                pass
