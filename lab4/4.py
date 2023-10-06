a = [int(s) for s in input().split()]
b = set()

for n in range(len(a)):
    if a[n] in b:
        print("YES")
    else:
        print("NO")
        b.add(a[n])
