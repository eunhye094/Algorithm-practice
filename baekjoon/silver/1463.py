x = int(input())

dp = [0 for i in range(x+1)]    #값 기록

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1     #1 더했을 때

    if i%2==0:
        dp[i]=min(dp[i], dp[i//2]+1)
    if i%3==0:
        dp[i]=min(dp[i], dp[i//3]+1)
    #둘 다 if 써야 +1, /2, /3 중 가장 좋은 방법 선택 가능

print(dp[x])