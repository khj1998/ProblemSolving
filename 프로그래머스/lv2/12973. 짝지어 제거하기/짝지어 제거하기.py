def solution(s):
    answer = -1
    temp = []
    
    for c in s:
        temp.append(c)
        temp_chr = temp[-2:]
        
        if len(temp)>=2 and temp_chr[0] == temp_chr[1]:
            temp.pop()
            temp.pop()
    
    if not temp:
        answer = 1
    else:
        answer = 0

    return answer