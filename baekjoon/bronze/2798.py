from itertools import combinations

n, m = map(int, input().split())
card = map(int, input().split())
ans = 0

for x in combinations(card, 3):
    if ans<=sum(list(x))<=m:
        ans=sum(list(x))

print(ans)