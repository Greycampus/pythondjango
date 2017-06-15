def arms(n):
    ns = str(n)
    summ = 0
    for i in range(0,len(ns)):
        summ = summ+int(ns[i])**3
    if(summ == n):
        return True
    else:
        return False
k = int(input('enter a number'))
if(arms(k)):
    print('%d is a armstrong number'%k)
else:
    print('%d is not a armstrong number'%k)
