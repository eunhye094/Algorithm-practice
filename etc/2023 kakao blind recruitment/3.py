from itertools import *

def solution(users, emoticons):
    sales = [i for i in [10, 20, 30, 40] if i>=min([x[0] for x in users])]
    emoticonSales = list(product((sales), repeat=len(emoticons)))
    bestCnt, bestTotal = 0, 0
   
    for i in emoticonSales:
        cnt, total = 0, 0
        for user in users:
            userTotal = 0
            for j in range(len(emoticons)):
                if i[j]>=user[0]:
                    userTotal+=(emoticons[j]-emoticons[j]*i[j]/100)
            if userTotal >= user[1]:
                cnt += 1
            else:
                total += userTotal
        if cnt>bestCnt or (cnt==bestCnt and total>bestTotal):
            bestCnt=cnt
            bestTotal=total
    print ([int(bestCnt), int(bestTotal)])
    return [int(bestCnt), int(bestTotal)]

solution([[40, 10000], [25, 10000]], [7000, 9000])
solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])