def generate_squares(N):
    for num in range (1,N+1):
        yield num **2
N=int(input())
squares_generator=generate_squares(N)
for square in squares_generator:
    print(square)