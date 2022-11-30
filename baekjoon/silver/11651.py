import sys
input = sys.stdin.readline

x = []
for _ in range(int(input())):
    x.append(list(map(int, input().split())))
x.sort(key=lambda x: (x[1], x[0]))
for i in x:
    print(i[0], i[1])