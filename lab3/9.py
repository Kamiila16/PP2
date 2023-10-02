a = [int(s) for s in input().split()]

for i in range(len(a)):
    if i%2==1:
        temp=a[i]
        a[i]=a[i-1]
        a[i-1]=temp
    
for i in range(len(a)):
    print(a[i])