def gcdd(n,m):
    if(max(n,m)%min(n,m)==0):
        return min(n,m)
    else:
        return gcdd(min(n,m),max(n,m)%min(n,m))
k = list(map(int,raw_input('enter two numbers').split(' ')))
print('The GCD is :%d'%gcdd(k[0],k[1]))
