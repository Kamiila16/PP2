def count_down(n):
    while n>=0:
        yield n
        n-=1
n=int(input())
count_down_generator=count_down(n)
for number in count_down_generator:
    print(number)