#문제 3. 최장 맨해튼 거리

a, b, c, d = map(int, input().split())
distance = [abs(a-b)+abs(c-d), abs(a-c)+abs(b-d), abs(a-d)+abs(b-c)]
print(max(distance))