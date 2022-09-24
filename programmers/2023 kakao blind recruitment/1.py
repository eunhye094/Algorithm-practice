from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    termsDic = {i.split()[0]: int(i.split()[1]) for i in terms}

    for i in range(len(privacies)):
        year, mon, day = privacies[i].split()[0].split('.')
        year, mon, day = int(year), int(mon), int(day)
        
        mon+=termsDic[privacies[i].split()[1]]
        while(mon>12):
            mon-=12
            year+=1

        if(datetime(int(today.split('.')[0]), int(today.split('.')[1]), int(today.split('.')[2])) >= datetime(year, mon, day)):
            answer.append(i+1)

    return answer

solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])