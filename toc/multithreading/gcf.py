#import threading
import threading
#globals used for function calls
k = 0
ff = 0
ll =[]
def inct():
    global k
    k=k+1
def incf():
    global ff
    ff=ff+1
def gcdd(m,n):
    if(k==0):
        #as given parameters are not users but thread need to started we used global to overwrite the parameters
        ll = list(map(int,input('enter two numbers:').split()))
        #making thread for factorial and setting target as fact function
        kk = threading.Thread(name = 'factorial',target=fact,args=(min(ll),))
        kk.start()
        inct()
        print(gcdd(ll[0],ll[1]))
    elif(max(m,n)%min(m,n)==0):
        return min(m,n)
    else:
        return gcdd(min(m,n),max(m,n)%min(m,n))
def fact(n):
    if(ff==0):
        incf()
        print(fact(n))
    elif(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)

#making thread for gcd 
t = threading.Thread(name='gcd',target=gcdd,args=(3,2))
t.start()
