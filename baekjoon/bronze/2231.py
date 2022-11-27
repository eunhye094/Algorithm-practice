n = int(input())

for x in range(1, n-1):
    if x+sum(list(map(int, str(x))))==n:
        print(x)
        exit()
        
print(0)