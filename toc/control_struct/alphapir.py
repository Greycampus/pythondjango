k = int(input('enter number:'))
w = int(input('enter width:'))
for i in range(0,k):
    print(str(chr(65+i)*(2*i+1)).center(w,'-'))
for i in range(1,k):
    print(str(chr(65+k-i-1)*(2*(k-i)-1)).center(w,'-'))
