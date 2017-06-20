equa = '1 -2 1'
quo = list(map(int,equa.split()))
mm = []
#derivative loop
for i in range(0,len(quo)):
    if(len(quo)-i-1!=0):
        mm.append((len(quo)-i-1)*quo[i])
print('After differentiation the equation:'+str(mm[0])+'x'+str( mm[1]))
mai = (-1*mm[1])/mm[0]
print('the maxima or minima of x2-2x+1 is at x=%d'%mai)
