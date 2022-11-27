a, b, c = int(input()), int(input()), int(input())

for i in range(10):
    print(str(a*b*c).count(str(i)))