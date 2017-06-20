def prim(n):
    if n>1:
        #loop for checking prime checking from 2 to square root of the number
        for i in range(2,int(n**0.5)):
            #if number is divisible then it is not prime so return false
            if(n%i==0):
                return False

        return True
    else:
        return False
#abs2 for finding prime that is at absolute difference of 1 with power of 2
#logic:
#user sends nth power of 2
#abs2 loops from oth power to nth power by checking the previous and next numbers of power of two whether it is prime or not
#if prime stores in list and returns the list at end
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
