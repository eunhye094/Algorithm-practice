import sys
input = sys.stdin.readline

n = []
for _ in range(int(input())):
    x = int(input())
    if x==0:
        n.pop()
    else:
        n.append(x)
print(sum(n))