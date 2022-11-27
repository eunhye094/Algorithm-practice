import sys
input = sys.stdin.readline

while True:
    x = input()[:-1]
    if x=='0':
        break
    if x == x[::-1]:
        print('yes')
    else:
        print('no')