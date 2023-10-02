a = [int(s) for s in input().split()]
k,c = [int(k) for k in input().split()]
a.append(0)

for i in reversed(range(k, len(a))):
    a[i]=a[i-1]
a[k]=c
    
for i in range (len(a)):
    print(a[i])
    
    