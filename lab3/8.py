a = [int(s) for s in input().split()]

elements = set()


for i in range(len(a)):
    elements.add(a[i])
    
print (len(elements))