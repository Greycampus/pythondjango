# works until input number <= 3486784401
# after that additional conditions appear for every ten digits increase
k = str(input('enter the number:'))
k1 = int(k)
ll = 2*len(k)
# range is checked based on length because for every two powers one digit increases
# storing the absolute difference in list
lk = [abs(k1-3**i) for i in range(ll-2,ll+2)]
# getting the minimum difference for getting nearest power
ans = min(lk)
print('the nearest power of three is:'+str(3**(ll-2+lk.index(ans))))
