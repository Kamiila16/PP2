def solve(numheads, numlegs):
    if numlegs%2!=0:
        return "Error"
    r=numlegs/2-numheads
    l=numheads-r
    return int(r),int(l)

numheads=35
numlegs=94
result=solve(numheads, numlegs)
print(result)
