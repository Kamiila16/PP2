a = [int(s) for s in input().split()]
cnt=0

            
for i in range(len(a)):
    for j in range (i,len(a)-1):
        if a[j+1]==a[i]:
            cnt=cnt+1
        
        
print (cnt)