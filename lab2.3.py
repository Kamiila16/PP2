r1=int(input())
s1=int(input())
r2=int(input())
s2=int(input())
if (r1+s1)%2==0 and (r2+s2)%2==0:
    print('YES')
elif (r1+s1)%2!=0 and (r2+s2)%2!=0:
        print('YES')
else:
    print('NO')