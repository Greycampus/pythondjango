def facta(n):
    if n==1 or n==0:
        return 1
    else:
        return n*facta(n-1)
k = int(input('enter the number to find its factorial'))
print('factorial is %d'%facta(k))
