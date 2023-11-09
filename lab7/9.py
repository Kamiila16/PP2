import re
input_string = input("Enter a string: ")
result_string = re.sub(r'([A-Z])', r' \1', input_string)
print("Modified String:", result_string)
