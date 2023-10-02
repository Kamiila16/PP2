a = [int(s) for s in input().split()]
x=int(input())

if x>a[0]:
    print (1)
    
elif x<a[len(a)-1]:
    print (len(a)+1)
    
for i in reversed(range(len(a))):
    if x==a[i]:
        print (i+2)
        break
    elif x>a[i] and x<a[i-1]:
        print(i+1)