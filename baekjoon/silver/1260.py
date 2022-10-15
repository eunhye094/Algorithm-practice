n, m, v = map(int, input().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited_dfs = [False for _ in range(n+1)]
visited_bfs = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    for w in range(1, n+1):
        if graph[v][w]==1 and not visited_dfs[w]:
            dfs(w)

def bfs(v):
    queue = [v]
    while queue:
        crnt = queue.pop(0)
        visited_bfs[crnt] = True
        print(crnt, end=' ')
        for w in range(1, n+1):
            if graph[crnt][w]==1 and not visited_bfs[w] and w not in queue:
                queue.append(w)

dfs(v)
print()
bfs(v)