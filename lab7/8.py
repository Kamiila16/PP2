import re
with open("row.txt", "r") as file:
    content = file.read()
split_strings = re.split(r'(?=[A-Z])', content)
print("Task 6: Split a string at uppercase letters:", split_strings