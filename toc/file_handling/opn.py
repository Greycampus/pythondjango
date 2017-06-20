#opeing the text file
f = open('text1.txt','r')
#getting nth line number from user
n = input('enter the line number:')
#split the file based on lines using \n escape code as \n indcates new line
dd = list(f.read().split('\n'))
if(len(dd)>=n+1):#checking if nth line exists in file or not
    print('%dth line:'%n+str(dd[n-1]))
else:
    print('no data')
