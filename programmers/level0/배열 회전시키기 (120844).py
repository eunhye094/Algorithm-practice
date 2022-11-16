def solution(numbers, direction):
    return numbers[1:]+[numbers[0]] if direction=='left' else [numbers[-1]]+numbers[:-1]
    # if direction=='right':
    #     numbers.insert(0, numbers.pop())
    # else:
    #     numbers.append(numbers.pop(0))
    # return numbers