def histogram(num):
    for i in range(num):
        print("*", end='')
    print('')

nums=[int(s) for s in input().split()]

for i in range (len(nums)):
    histogram(nums[i])