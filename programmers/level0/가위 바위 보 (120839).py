def solution(rsp):
    tmp={'2': '0', '0': '5', '5': '2'}
    return ''.join([tmp[i] for i in rsp])