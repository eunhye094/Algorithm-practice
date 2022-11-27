while True:
    x = list(map(int, input().split()))
    if x==[0,0,0]:
        break
    x.sort(reverse=True)
    if x[0]**2==x[1]**2+x[2]**2:
        print("right")
    else:
        print("wrong")