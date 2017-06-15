f = open('text1.txt','r')
n = input('enter the line number:')
dd = list(f.read().split('\n'))
if(len(dd)>=n+1):
    print('%dth line:'%n+str(dd[n-1]))
else:
    print('no data')
