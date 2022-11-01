import sys
input=sys.stdin.readline

s = input()[:-1] + ' '     #입력 문자열 \n 제거
stack = []
flag = False
ans = ""

for i in s:
    if i=='<':
        flag=True
        while stack:
            print(stack.pop(), end='')
        print(i, end='')
    elif i=='>':
        flag=False
        print(i, end='')
    elif flag:
        print(i, end='')
    else:
        if i==' ':
            while stack:
                print(stack.pop(), end='')
            print(' ', end='')
        else:
            stack.append(i)