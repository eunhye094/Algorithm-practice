#문제 1. 경로의 개수

island = int(input())
bridge = map(int, input().split())
route = 1

for i in bridge:
	route *= i

print(route)