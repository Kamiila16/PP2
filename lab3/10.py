a = [int(s) for s in input().split()]
min=1e10
max=-1e10
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
        max_index=i
    if a[i]<min:
        min=a[i]
        min_index=i
temp=a[min_index]
a[min_index]=a[max_index]
a[max_index]=temp

for i in range(len(a)):
    print(a[i])