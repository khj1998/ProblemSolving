def solution(info, n, m):
    dp = [-1] * (n+1)
    dp[0] = 0
    
    total_b_trace = sum(item[1] for item in info)
    
    for a_trace,b_trace in info:
        for j in range(n-1,a_trace-1,-1):
            if dp[j-a_trace] != -1:
                dp[j] = max(dp[j],dp[j-a_trace]+b_trace)
    
    for a_final_trace in range(n):
        if dp[a_final_trace] != -1:
            b_saved_trace = dp[a_final_trace]
            b_final_trace = total_b_trace - b_saved_trace
            
        if b_final_trace < m:
            return a_final_trace
    return -1
    
    return answer