for i in range(0,int(input('enter pyramid height:'))):
    #as we use only one variable i.e i
    #power of 10 -1 = largest number in its digit space
    #e.g 1000-1=999 =>999/9=111
    print(str((10**(i+1)-1)/9))
