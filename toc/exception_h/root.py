#defining the class for our exception
#our custom exception inherits the Exception class for raising the exception of complex roots
class complexerror(Exception):
    pass
#taking the input and splitting it and converting it into integer list using map and split function in python
k = list(map(int,raw_input('enter the equation in the form of 1 2 1 if equation is x^2 + 2x + 1:').split()))
try:
    t = k[1]**2-4*k[0]*k[2]
    if(t<0):
        #raising exception as determinant<0
        raise complexerror
    else:
        print('roots are :')
        print((-1*k[1]+float(t)**0.5)/(2*k[0]))
        print((-1*k[1]-float(t)**0.5)/(2*k[0]))
except complexerror:#exception body
    print('roots are complex so calculation stopped')
