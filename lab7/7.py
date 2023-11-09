import re
with open("row.txt", "r") as file:
    content = file.read()
snake_case_pattern = r'_(\w)'
camel_case_string = re.sub(snake_case_pattern, lambda x: x.group(1).upper(), content)
print( camel_case_string)
