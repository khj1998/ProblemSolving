def solution(land):
    answer = 0
    rows = len(land)
    dp = [[0]*4 for _ in range(rows)]
    
    for i in range(4):
        dp[0][i] = land[0][i]
    
    for i in range(1,rows):
        dp[i][0] = max(dp[i][0],land[i][0]+max(dp[i-1][1],dp[i-1][2],dp[i-1][3]))
        dp[i][1] = max(dp[i][1],land[i][1]+max(dp[i-1][0],dp[i-1][2],dp[i-1][3]))
        dp[i][2] = max(dp[i][2],land[i][2]+max(dp[i-1][0],dp[i-1][1],dp[i-1][3]))
        dp[i][3] = max(dp[i][3],land[i][3]+max(dp[i-1][0],dp[i-1][1],dp[i-1][2]))
    
    return max(dp[rows-1])