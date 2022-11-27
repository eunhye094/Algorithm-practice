a = []

for _ in range(int(input())):
    a.append(list(map(int, input().split())))

a.sort(key=lambda x: (x[0], x[1]))

for x in a:
    print(x[0], x[1])