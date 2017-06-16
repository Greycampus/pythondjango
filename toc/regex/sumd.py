import re
k= str(raw_input('enter the alphanumeric string'))
k = re.sub(r"[a-zA-Z]+",'',k)
summ = sum(int(i) for i in k)
print('the sum is %d'%summ)
