def spy_game(nums):
    
    lol_0 = False
    lol_00 = False

    
    for num in nums:
        if num == 0:
            if not lol_0:
                lol_0 = True
            elif lol_0 and not lol_00:
                lol_00 = True
        elif num == 7 and lol_00:
            return True

    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5])) 