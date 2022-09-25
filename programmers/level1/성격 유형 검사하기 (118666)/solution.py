def solution(survey, choices):
    answer = ''
    type = ['RT', 'CF', 'JM', 'AN']
    score = {x[i] : 0 for x in type for i in range(2)}
    for i in range(len(survey)):
        if(choices[i]<4):
            score[survey[i][0]]+=(4-choices[i])
        elif(choices[i]>4):
            score[survey[i][1]]+=(choices[i]-4)

    for i in type:
        if(score[i[0]]>=score[i[1]]): answer+=i[0]
        else: answer+=i[1]
    print(answer)
    return answer

solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])   #"TCMA"
solution(["TR", "RT", "TR"], [7, 1, 3]) #RCJA
