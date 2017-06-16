class complexerror(Exception):
    pass
k = list(map(int,raw_input('enter the equation in the form of 1 2 1 if equation is x^2 + 2x + 1:').split()))
try:
    t = k[1]**2-4*k[0]*k[2]
    if(t<0):
        raise complexerror
    else:
        print('roots are :')
        print((-1*k[1]+float(t)**0.5)/(2*k[0]))
        print((-1*k[1]-float(t)**0.5)/(2*k[0]))
except complexerror:
    print('roots are complex so calculation stopped')
