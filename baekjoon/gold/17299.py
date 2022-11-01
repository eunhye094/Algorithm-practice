import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
cnt = {}
stack = []
ans = [-1] * n

for i in a:     #list.count 사용 시, 시간 초과 → 2중 for문과 동일
    if not cnt.get(i):
        cnt[i]=1
    else:
        cnt[i]+=1

for i in range(n):
    while stack and cnt[a[stack[-1]]]<cnt[a[i]]:
        ans[stack.pop()]=a[i]
    stack.append(i)
        
for i in ans:
    print(i, end=' ')