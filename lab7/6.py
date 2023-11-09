import re
with open("row.txt", "r") as file:
    content = file.read()
content_with_colons = re.sub(r'[ ,.]', ':', content)

