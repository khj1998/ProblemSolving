def solution(n, tops):
    answer = 0
    prev_0 = 0
    prev_1 = 1
    MOD = 10007
    
    for i in range(1,n+1):
        value = 3
        
        if tops[i-1] == 1:
            value = 4
        
        answer = (prev_1*value - prev_0)%MOD
        
        prev_0,prev_1 = prev_1,answer
        
    return answer