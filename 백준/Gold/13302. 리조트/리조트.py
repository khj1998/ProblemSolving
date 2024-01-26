import sys
input = sys.stdin.readline

N,M = map(int,input().split())
INF = int(1e7)
array = list(map(int,input().split()))
dp = [[INF]*80 for _ in range(N+6)]
dp[0][0] = 0

for i in range(N+1):
    for j in range(40):
        if dp[i][j] == INF:
            continue

        if i+1 in array:
            dp[i+1][j] = min(dp[i][j],dp[i+1][j])
            continue

        dp[i+1][j] = min(dp[i][j]+10000,dp[i+1][j])

        for k in range(1,4):
            dp[i+k][j+1] = min(dp[i+k][j+1],dp[i][j]+25000)

        for k in range(1,6):
            dp[i+k][j+2] = min(dp[i+k][j+2],dp[i][j]+37000)

        if j>=3:
            dp[i+1][j-3] = min(dp[i+1][j-3],dp[i][j])

print(min(dp[N]))
