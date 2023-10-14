def filter_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    flag=True
    for i in range (2,n):
        if n%i==0:
            flag=False
            break
    return flag
        

a=[int(s) for s in input().split()]
for i in range (len(a)):
    if filter_prime(a[i]):
        print (a[i], end=" ")