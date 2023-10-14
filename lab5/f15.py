from itertools import permutations

def perms(s):
    p = permutations(s)
    for i in p:
        print(''.join(i))

s = input()

perms(s)