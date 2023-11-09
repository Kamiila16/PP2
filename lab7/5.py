import re
with open("row.txt", "r") as file:
    content = file.read()
a_followed_by_b_pattern = r'a.*b$'
matches_a_b = re.search(a_followed_by_b_pattern, content)
print( matches_a_b )