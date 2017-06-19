import re
k = str(raw_input('enter the string:'))
#replacing the pattern in string
k = re.sub(r"\[!\*\]",'',re.sub(r"\[!\*\]",'',k))
print(k)
