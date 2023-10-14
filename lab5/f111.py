def palindrome(s):
    if s[::-1]==s:
        return True
    return False
    
s=palindrome(input())
print(s)