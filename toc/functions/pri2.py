def prim(n):
    if n>1:
        for i in range(2,int(n**0.5)):
            if(n%i==0):
                return False

        return True
    else:
        return False
def abs2(n):
    k = []
    for i in range(0,n+1):
        tm = 2**i
        if(prim(tm-1)):
            k.append(tm-1)
        elif(prim(tm+1)):
            k.append(tm+1)
    return list(set(k))
k = int(input('enter nth term upto which you wish check:'))
print('the primes that are exactly at absolute difference of 1 with powers of two below %d are'%(2**k))
print(abs2(k))
