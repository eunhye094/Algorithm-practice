from itertools import combinations

n, m = map(int, input().split())
ice = [[True for _ in range(n+1)] for _ in range(n+1)]
ans = 0

for _ in range(m):
    a, b = map(int, input().split())
    ice[a][b], ice[b][a] = False, False

for p in combinations([i for i in range(1, n+1)], 3):
    #in으로 배열 내 유무 확인하면 시간 초과 → True/False 확인으로 해결
    if ice[p[0]][p[1]] and ice[p[1]][p[2]] and ice[p[2]][p[0]]:
        ans+=1

print(ans)