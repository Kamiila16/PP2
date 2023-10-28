def squares(a,b):
    for num in range(a,b+1):
        yield num** 2
a=int(input())
b=int(input())
squares_generator=squares(a,b)
for square in squares_generator :
    print(square)
