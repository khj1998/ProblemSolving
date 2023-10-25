from collections import deque

dx,dy=[1,0],[0,1]

def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for p in puddles:
        dp[p[1]][p[0]] = -1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            
            dp[i][j] += (dp[i-1][j] + dp[i][j-1]) % 1000000007
    print(dp)
    return dp[n][m]