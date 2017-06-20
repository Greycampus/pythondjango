#armstrong number function
def arms(n):
    #converting n into string so we can access each digit individually using the string indexing 
    ns = str(n)
    #summ variable for comparsion
    summ = 0
    for i in range(0,len(ns)):
        #summing the cubes of each digit into summ variable
        summ = summ+int(ns[i])**3
    if(summ == n):#comparing the summ and n to check the equality
        return True
    else:
        return False
k = int(input('enter a number'))
if(arms(k)):
    print('%d is a armstrong number'%k)
else:
    print('%d is not a armstrong number'%k)
