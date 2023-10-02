a = [int(s) for s in input().split()]
index=0
for i in range(len(a)):
    n=max(a)
    if a[i]==n:
        index=i
        break
print(n,index)
   