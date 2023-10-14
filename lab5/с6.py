def primes(n):
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
res=list(filter(lambda x: primes(x), a))
print(res)