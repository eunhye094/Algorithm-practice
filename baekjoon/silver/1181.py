words = []
for _ in range(int(input())):
    word = input()
    if word not in words:
        words.append(word)
words.sort(key=lambda x: (len(x), x))
for w in words:
    print(w)