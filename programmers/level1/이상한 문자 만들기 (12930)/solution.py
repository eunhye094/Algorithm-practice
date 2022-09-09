def solution(s):
    answer = ''
    index = 0
    for i in range(len(s)):
        if s[i]==' ':
            answer+=' '
            index = 0
        else:
            answer+=s[i].upper() if index%2==0 else s[i].lower()
            index += 1
    return answer