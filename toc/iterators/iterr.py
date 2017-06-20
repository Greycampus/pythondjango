#importing iteration tools
import itertools
def multiples(n):
        #using combinations and generating the multiples of 2 and 3(both) i.e multiples of 6
        k = itertools.combinations([6*i for i in range(1,n+1)],1)
        ll = [k.next()[0] for i in range(0,n)]
        return ll
print(multiples(int(input('enter the nth term:'))))
