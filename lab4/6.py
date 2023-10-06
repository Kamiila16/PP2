num_lines = int(input())
words = set()
for _ in range(num_lines):
    l = input()
    w = l.split()
    words.update(w)
print(len(words))