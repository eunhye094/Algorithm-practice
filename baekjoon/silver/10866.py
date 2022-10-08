import sys
from collections import deque

d = deque()

for _ in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()

    if(cmd[0]=='push_front'):
        d.appendleft(cmd[1])
    elif(cmd[0]=='push_back'):
        d.append(cmd[1])
    elif(cmd[0]=='pop_front'):
        if d: print(d.popleft())
        else: print(-1)
    elif(cmd[0]=='pop_back'):
        if d: print(d.pop())
        else: print(-1)
    elif(cmd[0]=='size'):
        print(len(d))
    elif(cmd[0]=='empty'):
        if d: print(0)
        else: print(1)
    elif(cmd[0]=='front'):
        if d: print(d[0])
        else: print(-1)
    elif(cmd[0]=='back'):
        if d: print(d[-1])
        else: print(-1)