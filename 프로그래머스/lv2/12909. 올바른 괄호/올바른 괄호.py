def solution(s):
    stack = []

    if s[0] == ")":
        return False
    
    for i in s:
        if i=='(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
    
    return len(stack)==0