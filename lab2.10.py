r1=int(input())
s1=int(input())
r2=int(input())
s2=int(input())
if abs(r1-r2)==abs(s1-s2):
        print ('YES')
elif (r1+r2)<=8 and s1+s2<=8 or abs(r1-r2)<=8 and abs(s1-s2)<=8 :
    print('YES')
elif ((r1+r2)<=8 and s1+s2<=8 or abs(r1-r2)<=8 and abs(s1-s2)<=8 )and abs(r1-r2)==abs(s1-s2) :
    print('YES')
else:
    print('NO')