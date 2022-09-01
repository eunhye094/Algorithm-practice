def solution(priorities, location):
    answer = 0
    empty = 0
    queue = []

    while (priorities):
        empty = priorities.pop(0)
        location -= 1

        if (not priorities):
            answer += 1
            return answer
        if (empty >= max(priorities)):
            answer += 1
            if (location == -1):
                return answer
        else:
            priorities.append(empty)
            if (location == -1):
                location = len(priorities) - 1

    return answer