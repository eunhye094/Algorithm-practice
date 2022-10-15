import sys

n, m = map(int, sys.stdin.readline().split())
graph = [set() for _ in range(n)]
visited = [False for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)

def dfs(v, depth):
    visited[v] = True
    if depth==4:
        print(1)
        exit()                  #프로그램 종료
    for i in graph[v]:
        if not visited[i]:
            dfs(i, depth+1)     #재귀함수 호출 수 = 그래프 깊이
    visited[v] = False

for i in range(n):
    dfs(i, 0)

print(0)