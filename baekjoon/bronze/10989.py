#일반 방법 사용하면 메모리 초과

import sys
input = sys.stdin.readline

#입력 개수는 최대 10,000,000이지만 입력 정수의 최댓값이 10,000
num = [0] *10001
for _ in range(int(input())):
    num[int(input())]+=1
for i in range(len(num)):
    for j in range(num[i]):
        print(i)