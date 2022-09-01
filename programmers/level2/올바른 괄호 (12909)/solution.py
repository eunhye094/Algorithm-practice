def solution(s):
    stack = []
    for i in range(len(s)):
        if (s[i]=='('):
            stack.append(s[i])
        else:
            if not stack:
                return False
            else:
                stack.pop()
    if not stack :
        return True
    else:
        return False