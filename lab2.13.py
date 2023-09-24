N=int(input())
M=int(input())
x=int(input())
y=int(input())
if N>M:
    t=N
    N=M
    M=t
    
if N-x>x:
    res=x
elif N-x<x:
    res=N-x
if M-y>y:
    res2=y
elif M-y<y:
    res2=M-y
if res>res2:
    print(res2)
else:
    print(res)
    