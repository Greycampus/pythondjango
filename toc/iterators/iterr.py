import itertools
def multiples(n):
        k = itertools.combinations([6*i for i in range(1,n+1)],1)
        ll = [k.next()[0] for i in range(0,n)]
        return ll
print(multiples(int(input('enter the nth term:'))))
