n, k = map(int, input().split())
people = list(range(1, n+1))
target = 0
ans = []

for _ in range(n):
    target += k-1
    target %= len(people)
    ans.append(str(people.pop(target)))

print('<'+', '.join(ans)+'>')