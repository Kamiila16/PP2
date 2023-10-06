a=set(int(s) for s in input().split())
b=set(int(i) for i in input().split())
print(*sorted(set(a.intersection(b))), key=int)