import re
with open("row.txt", "r") as file:
    content = file.read()
sequence_underscore_pattern = r'[a-z]+_[a-z]+'
sequences_underscore = re.findall(sequence_underscore_pattern, content)
print( sequences_underscore)
