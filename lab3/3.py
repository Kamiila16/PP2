a = [int(s) for s in input().split()]
n=len(a)
for i in range(n-1):
    if(a[i+1]>a[i] ):
        print(a[i+1])