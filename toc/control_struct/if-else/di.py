#equation x3+4x2+2x-1
equa = '1 4 2 -1'
#spliting string into int list using map and split
quo = list(map(int,equa.split()))
mm = []
#integration loop for getting integration of equation
for i in range(0,len(quo)):
    if(len(quo)-i-1!=0):
        mm.append((len(quo)-i-1)*quo[i])
print('after differentiation the equation is:'+str(mm[0])+'x2+'+str(mm[1])+'x+'+str(mm[2]))
dd = [len(quo)-i for i in range(0,len(quo))]
print('after integration the equation is:'+str(quo[0])+'/'+str(dd[0])+'x4 + '+str(quo[1])+'/'+str(dd[1])+'x3 + '+str(quo[2])+'/'+str(dd[2])+'x2 + '+str(quo[3])+'/'+str(dd[3])+'x + '+'c')
