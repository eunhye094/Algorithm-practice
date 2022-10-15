import sys

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
cnt = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(v):
    queue = [v]
    while queue:
        crnt = queue.pop(0)
        visited[crnt] = True
        for i in graph[crnt]:
            if not visited[i] and i not in queue:
                queue.append(i)

# def bfs(v):
#     queue = [v]
#     visited[v]=True
#     while queue:
#         crnt = queue.pop(0)
#         for i in graph[crnt]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i]=True

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt+=1

print(cnt)