num = []
for i in range(10):
    temp = int(input())%42
    if temp not in num:
        num.append(temp)
print(len(num))