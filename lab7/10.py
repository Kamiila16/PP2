import re
with open("row.txt", "r") as file:
    content = file.read()
camel_case_to_snake_case = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', content).lower()
print( camel_case_to_snake_case)
