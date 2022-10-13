#문제 4. 폭탄 구현하기

import numpy

n, k = map(int, input().split())
square = numpy.array([[0 for _ in range(n)] for _ in range(n)])

for i in range(k):
	a, b = map(int, input().split())
	a-=1
	b-=1
	square[a][b]+=1
	if(a!=0): square[a-1][b]+=1
	if(a!=n-1): square[a+1][b]+=1
	if(b!=0): square[a][b-1]+=1
	if(b!=n-1):square[a][b+1]+=1

print(square.sum())