def solution(s):
    stack = []
    
    for c in s:
        if not stack:
            stack.append(c)
            continue
        if c == ')':
            temp = stack.pop()
            
            if temp != '(':
                stack.append(c)
                stack.append(temp)
            
        else:
            stack.append(c)
        
    return len(stack) == 0