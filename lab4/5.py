N, M = map(int, input().split())
colors_ani = set()
colors_borya = set()
for _ in range(N):
    color = int(input())
    colors_ani.add(color)
for _ in range(M):
    color = int(input())
    colors_borya.add(color)
cc = colors_ani.intersection(colors_borya)
ua = colors_ani.difference(colors_borya)
ub = colors_borya.difference(colors_ani)
print(len(cc))
print(*sorted(cc))

print(len(ua))
print(*sorted(ua))

print(len(ub))
print(*sorted(ub))