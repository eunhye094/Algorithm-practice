import sys
input = sys.stdin.readline
from collections import deque

q = deque()

for _ in range(int(input())):
    x = input().split()
    if x[0]=='push':
        q.append(int(x[1]))
    if x[0]=='pop':
        print(q.popleft()) if len(q)!=0 else print(-1)
    if x[0]=='size':
        print(len(q))
    if x[0]=='empty':
        print(0) if len(q)!=0 else print(1)
    if x[0]=='front':
        print(q[0]) if len(q)!=0 else print(-1)
    if x[0]=='back':
        print(q[-1]) if len(q)!=0 else print(-1)