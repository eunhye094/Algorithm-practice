def solution(id_list, report, k):
    userIdx = {}
    user = {}
    reported = {}
    answer = []

    for i in range(len(id_list)):
        userIdx[id_list[i]] = i
        user[id_list[i]] = []
        reported[id_list[i]] = 0
        answer.append(0)

    for i in report:
        a, b = i.split()
        if b not in user[a]:
            user[a].append(b)
            reported[b]+=1

    for key1, value1 in reported.items():
        if value1>=k:
            for key2, value2 in user.items():
                if key1 in value2:
                    answer[userIdx[key2]]+=1

    return answer
