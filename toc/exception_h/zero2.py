#creating custom exception by inheriting the Exception class
class zeroor2(Exception):
    pass
#function for getting the prime factors
#it is used in finding the powers of 2
#if a number is power of two then the unique number of prime factors are same and equal to
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac
class expe():
    """docstring forexpe."""
    def __init__(self,q):
        self.q=q
    def ddd(self,qt,wt):
        try:
            if(wt==0 or (len(set(primes(wt)))==1 and list(set(primes(wt)))[0]==2)):
                #condtion checking for divisor equal to 0 or power of
                #raising zero or power of 2 exception
                raise zeroor2
            else:
                print(primes(wt))
                print(qt/wt)
        except zeroor2:
            print('shouldnt be divided by zero or a power of 2')
k = expe('q')
inp1 = input('enter the divident:')
inp2 = input('enter divisor:')
k.ddd(inp1,inp2)
