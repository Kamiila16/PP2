import re
with open('row.txt') as file:
    content = file.read()
pattern = 'а.*б'
if re.findall(pattern, content):
    print()
else:
    print("No match found.")
