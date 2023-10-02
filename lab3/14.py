

a = [int(s) for s in input().split()]

for i in range (len(a)):
    for j in range (len(a)):
        if a[i]==a[j] and i!=j:
            break
    else:
        print(a[i])
    

    