import sys
input=sys.stdin.readline
from collections import deque

n,m,r=map(int, input().split())
graph=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque([r])
visited[r] = tmp = 1

while(q):
    cur=q.popleft()
    graph[cur].sort()
    for i in graph[cur]:
        if visited[i]==0:
            tmp+=1
            visited[i]=tmp
            q.append(i)

for i in visited[1::]:
    print(i)