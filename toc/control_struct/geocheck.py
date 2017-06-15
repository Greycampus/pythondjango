a = int(input('enter initial term:'))
r = int(input('enter ratio in series:'))
k = int(input('enter number you want to check:'))
if(k%a==0 and k==a):
    print('you just entered the initial term again,yes its in series')
elif(k%a==0 and k%r==0 and k>a):
    tmp = k/a
    while tmp!=1 and tmp >=r:
        tmp=tmp/r
    if(tmp==1):
        print('%d is in series'%k)
    else:
        print('%d is not in series'%k)
else:
    print('%d is not in series'%k)
