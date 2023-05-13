def solution(t, p):
    answer=0
    max_len = len(t)
    s_len = len(p)
    start = 0
    end = s_len
    
    while end <= max_len:
        temp = t[start:end]
        
        if int(temp) <= int(p):
            answer+=1
        start+=1
        end+=1
    
    return answer