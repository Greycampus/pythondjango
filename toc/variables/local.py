# works until input number <= 3486784401
# after that additional conditions appear for every ten digits increase
k = str(input('enter the number:'))
k1 = int(k)
ll = 2*len(k)
lk = [abs(k1-3**i) for i in range(ll-2,ll+2)]
ans = min(lk)
print('the nearest power of three is:'+str(3**(ll-2+lk.index(ans))))
