def solution(num, total):
    return [i for i in range(total//num-(num//2)+(0 if num%2 else 1), total//num+(num//2)+1)]