def solution(n):
    answer = 0
    dp = [0]*(n+1)
    dp[1] = 1
    if n>=2:
        dp[2]=2
    
    for idx in range(3,n+1):
        dp[idx] = dp[idx-1] + dp[idx-2]
    return dp[n]%1234567