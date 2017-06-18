import threading
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
        ll = list(map(int,input('enter two numbers:').split()))
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

#try:
    #thread.start_new_thread(print(gcdd(ll[0],ll[1])))
    #thread.start_new_thread(print(fact(min(ll))))
#except Exception as e:
#    raise
t = threading.Thread(name='gcd',target=gcdd,args=(3,2))
t.start()

