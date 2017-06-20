#importing threads from threading
from threading import Thread
i = 1
j = 1
k = 1
def runA():
        global i
        while(i<=k):
                #print multiple of 2
                print(str(int(2*i))+' ')
                i+=1

def runB():
        global j
        while(j<=k):
            #print multiple of 3
                print(str(int(3*j))+' ')
                j+=1

if __name__ == "__main__":
        k = int(input('enter the nth term:'))
        #setting target for threads
        t1 = Thread(target = runA)
        t2 = Thread(target = runB)
        #setting daemon
        t1.setDaemon(True)
        t2.setDaemon(True)
        #starting threads
        t1.start()
        t2.start()
        #while for running of threads
        while i<=k and j<=k:
                pass
