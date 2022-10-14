#아리스토테네스의 체
n = 1000000
check = [False, False] + [True for _ in range(n-1)]
for i in range(2, n+1):
    if check[i]:
        for j in range(i*2, n+1, i):
        	check[j]=False

while True:
    n = int(input())
    
    if(n==0): break

    for i in range(3, n//2+1, 2):
        if check[i] and check[n-i]:
            print(n,"=",i,"+",n-i)
            break
    else:
        print("Goldbach's conjecture is wrong.")