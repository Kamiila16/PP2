def even_numbers_generator(n):
    for num in range(0,n+1,2):
        yield num
n=int(input())
even_numbers=even_numbers_generator(n)
even_coma=', '.join(map(str,even_numbers))
print(even_coma)