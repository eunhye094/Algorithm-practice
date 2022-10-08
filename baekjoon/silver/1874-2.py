#참고한 코드
#32816KB, 3832ms

cnt = int(input())
num = 1
stack, result = [], []
flag = True

for i in range(cnt):
    target = int(input())
    while num<=target:
        stack.append(num)
        result.append('+')
        num+=1
    if stack[-1]==target:
        stack.pop()
        result.append('-')
    else:   #target이 이미 넣어진 상태, 즉 더 아래에 있다는 의미
        print("NO")
        flag = False
        break

if flag:
    print('\n'.join(result))