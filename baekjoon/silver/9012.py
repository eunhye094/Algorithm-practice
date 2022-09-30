import sys

cnt = int(sys.stdin.readline())

for _ in range(cnt):
    stack = []
    ps = sys.stdin.readline()
    for i in ps:
        if i=="(":
            stack.append(i)
        elif i==")":
            if not stack:
                print("NO")
                break
            else:
                stack.pop()
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
    