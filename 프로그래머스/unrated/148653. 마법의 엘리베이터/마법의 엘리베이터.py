def solution(storey):
    answer = 0
    
    while storey > 0:
        r = storey%10
        
        if r < 5:
            answer += r
        elif r > 5:
            answer += (10-r)
            storey += 10
        else:
            if (storey//10)%10 > 4:
                storey += 10
                
            answer += 5
        
        storey = storey//10

    return answer