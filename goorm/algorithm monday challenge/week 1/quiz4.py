#문제 4. 소수 찾기

import math

def is_prime_number(n):
	if n==1:
		return False
	for i in range(2, int(math.sqrt(n)+1)):
		if n%i==0:
			return False
	return True

cnt = int(input())
num = list(map(int, input().split()))
prime = [num[i] for i in range(cnt) if is_prime_number(i+1)]
print(sum(prime))