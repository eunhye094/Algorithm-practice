for _ in range(int(input())):
    r, s = input().split()
    print(''.join([x*int(r) for x in s]))