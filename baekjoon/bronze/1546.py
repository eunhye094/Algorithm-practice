input()
score = list(map(int, input().split()))
avg = sum(score)/len(score)/max(score)*100
print(avg)