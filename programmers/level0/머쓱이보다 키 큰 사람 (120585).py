def solution(array, height):
    # array.sort()
    # for i in range(len(array)):
    #     if array[i]>height:
    #         return len(array[i:])
    # return 0
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)