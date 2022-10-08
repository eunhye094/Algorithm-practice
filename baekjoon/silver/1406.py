# 커서를 기준으로 좌우 stack을 나눈 것
# append/pop만을 사용하기 위해 오른쪽 stack은 문자열을 반대로 사용 (ex. ABC > CBA)

import sys

left = list(sys.stdin.readline().rstrip())
right = []

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if(command[0]=='L'):
        if left:
            right.append(left.pop())
    elif(command[0]=='D'):
        if right:
            left.append(right.pop())
    elif(command[0]=='B'):
        if left:
            left.pop()
    elif(command[0]=='P'):
        left.append(command[1])

left.extend(reversed(right))
print(''.join(left))