from itertools import permutations

def solution(spell, dic):
    word = [''.join(i) for i in list(permutations(spell))]
    for d in dic:
        if d in word: 
            return 1
            exit()
    return 2