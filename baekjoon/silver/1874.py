#내가 짠 코드
#35744KB, 5900ms

cnt = int(input())
target, stack, result = [], [], []

for i in range(cnt):
    target.append(int(input()))

for i in range(1, cnt+1):
    stack.append(i)
    result.append('+')
    while(len(stack)!=0 and stack[-1]==target[0]):
        target.pop(0)
        stack.pop()
        result.append('-')

if target:
    print("NO")
else:
    print('\n'.join(result))