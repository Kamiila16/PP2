n, k = [int(s) for s in input().split()]
a = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        a[j] = '.'
for i in range(n):
   print(a[i], end='')
        