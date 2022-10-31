import sys
input=sys.stdin.readline
from collections import deque

v=int(input())
e=int(input())
graph=[[] for _ in range(v+1)]
visited=set([1])
q=deque([1])

for _ in range(e):
    a, b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

while q:
    cur=q.popleft()
    for i in graph[cur]:
        if i not in visited:
            visited.add(i)
            q.append(i)

print(len(visited)-1)