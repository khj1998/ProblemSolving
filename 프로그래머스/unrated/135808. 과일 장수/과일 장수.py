def solution(k, m, score):
    answer = 0
    num = 0
    min_val = 10
    score.sort()
    score.reverse()
    
    for s in score:
        num+=1
        min_val = min(s,min_val)
        if num%m==0:
            answer += (min_val*m)
            min_val = 10
        
    return answer