import re
with open("row.txt", "r") as file:
    content = file.read()
pattern = r'аб{2,3}'
if re.search(pattern, content):
    print()
else:
    print("No match found.")
lllm,