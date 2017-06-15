def votec(sr):
    lsr = [s for s in sr]
    ssr = list(set(lsr))
    maz= 0
    party = ''
    for i in range(0,len(ssr)):
        if(lsr.count(ssr[i])>maz):
            maz=lsr.count(ssr[i])
            party = ssr[i]
        elif(lsr.count(ssr[i])==maz):
            party = party+ssr[i]
    return [party,maz]
k = raw_input('enter the vote string:')
result = votec(k)
if(len(result[0])>1):
    print('it\'s a tie between %s'%result[0])
    print('with hightest votes %d'%result[1])
else:
    print('the winner is '+result[0]+' party with '+str(result[1])+' votes')
