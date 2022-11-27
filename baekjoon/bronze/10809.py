import string

s = input()

for a in string.ascii_lowercase:
    if a in s:
        print(s.index(a), end=" ")
    else:
        print(-1, end=" ")