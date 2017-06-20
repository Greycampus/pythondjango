k = int(input('enter total number of mediums: '))
l = int(input('enter length of medium: '))
h = int(input('enter height from which ball is thrown: '))
d = int(input('enter distance travelled in each step:'))
print('now enter qoutients of loss for %d mediums:'%k)
kq =[]
for i in range(0,k):
    kq.append(float(input('%d medium :'%(i+1))))
h1 = h
d1 = 0
while h1!=0:
    fl = k*l
    for i in range(0,k): #for medium check
        if (h1!=0): #height not equal to zero
            tt = d1%fl #medium repeatition check
            d1=d1+d #distance increament per step
            h1 = int(h1*(1-kq[int(tt/l)]))
print('distance traveled by ball is %d'%d1)
