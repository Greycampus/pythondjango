#program for list to string
# its ok if you are unable to do it as it uses list comprehensions
k =[1,2,3,4,5,6]
print('list taken:')
print(k)
string = ''.join(str(i) for i in k)
print('converted string:'+string)
