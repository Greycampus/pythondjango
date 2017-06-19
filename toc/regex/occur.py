import re
k = raw_input('enter the main string:')
s = raw_input('enter the symbol you wish find occurences:')
#replacing input symbol in the string and find the decrease in lenth to find the occurences
k1 = re.sub(r''+s+'','',k)
print(s+' occured '+str(len(k)-len(k1))+' times in '+k)
