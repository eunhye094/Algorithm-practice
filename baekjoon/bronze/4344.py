for i in range(int(input())):
    num, *score = map(int, input().split())
    avg = sum(score)/len(score)
    cnt = 0
    for j in range(len(score)):
        if score[j]>avg:
            cnt+=1
    print("{:.3f}%".format(cnt/len(score)*100))