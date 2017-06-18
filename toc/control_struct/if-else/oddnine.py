k = int(input())
if(k%2!=0 and k%9==0):
    print('%d is both odd and multiple of 9'%k)
elif(k%2!=0 and k%9!=0):
    print('%d is odd but not multiple of 9'%k)
elif(k%2==0 and k%9==0):
    print('%d is not odd but a multiple of 9'%k)
else:
    print('%d is not odd and multiple of 9'%k)
