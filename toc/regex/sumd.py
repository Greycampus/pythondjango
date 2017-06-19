import re
k= str(raw_input('enter the alphanumeric string'))
#replace the all characters with null
k = re.sub(r"[a-zA-Z]+",'',k)
#find sum
summ = sum(int(i) for i in k)
print('the sum is %d'%summ)
