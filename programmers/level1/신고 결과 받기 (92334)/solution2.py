def solution(id_list, report, k):
    reportCnt = {x: 0 for x in id_list}
    answer = [0] * len(id_list)

    for i in set(report):
        reportCnt[i.split()[1]]+=1
    
    for i in set(report):
        if reportCnt[i.split()[1]]>=k:
            answer[id_list.index(i.split()[0])]+=1

    return answer
