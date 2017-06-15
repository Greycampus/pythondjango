f1 = open('text.txt','r').read()
f2 = open('text1.txt','r').read()
f3 = open('text2.txt','w').write(str(f1)+str(f2))

f  = open('text2.txt','r').read()
print('appended file data:')
print(f)
