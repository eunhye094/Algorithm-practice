#문제 1. 합격자 찾기

for i in range(int(input())):
	success = 0
	n = int(input())
	v = list(map(int, input().split()))
	avg = sum(v)/len(v)
	for i in v:
		if i>=avg:
			success+=1
	print('{}/{}'.format(success, n))