def solution(scores):
    answer = 1
    wanho_a,wanho_b = scores[0][0],scores[0][1]
    scores.sort(key = lambda x:(-x[0],x[1]))
    max_b = 0
    
    for a,b in scores:
        if wanho_a < a and wanho_b < b:
            return -1
        
        if b >= max_b:
            max_b = b
            
            if a + b > wanho_a + wanho_b:
                answer += 1
    
    return answer