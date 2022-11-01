#이중 for문 O(n^2) → stack O(n)
#주석은 내 풀이, 최종은 참고 → 메모리 절반 절약!

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
stack = []

ans = [-1]*n    #변경 안 하면 자동 -1

for i in range(n):
    while stack and a[stack[-1]]<a[i]:
        ans[stack.pop()]=a[i]    #스택 안쪽이 더 클 수 밖에 없음!
    stack.append(i)

for i in ans:
    print(i, end=' ')

# ans = {}

# for i in range(n):
#     while stack and stack[-1][1]<a[i]:
#         x=stack.pop()
#         ans[x[0]]=a[i]
#     stack.append([i, a[i]])

# while stack:
#     x=stack.pop()
#     ans[x[0]]=-1

# for i in range(n):
#     print(ans[i], end=' ')