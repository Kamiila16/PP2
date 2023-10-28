def db3_4_generator(n):
    for num in range(0,n+1):
        if num%3==0 and num%4==0:
            yield num
n=50
db=db3_4_generator(n)
for num in db:
    print(num)