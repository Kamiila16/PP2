def unique(nums):
    res=[]
    for x in nums:
        if x not in res:
            res.append(x)
    return res

nums=[int(s) for s in input().split()]
ans=unique(nums)
print(ans)