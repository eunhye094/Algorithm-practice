import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
card = defaultdict(int)
for x in map(int, input().split()):
    card[x]+=1

m = int(input())
for x in map(int, input().split()):
    print(card[x], end=' ')