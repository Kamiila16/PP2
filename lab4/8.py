a=set()
b=set()
for i in range(1,int(input())+1): a.add(i)
n=len(a)
while True:
    c=input()
    if c=='HELP':
        break
    else:
        c={int(y) for y in c.split()}
        c-=b
        if len(c)<(n-len(b))//2+1:
            print('NO')
            a-=c
            b|=c
        elif len(c)>(n-len(b))//2:
            print('YES')
            a&=c
            b|=c-a
print(*sorted(a))