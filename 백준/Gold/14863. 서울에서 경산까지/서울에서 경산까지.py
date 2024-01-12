import sys
input = sys.stdin.readline

N,K = map(int,input().split())
roads = [[] for _ in range(N+1)]
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    a,b,c,d = map(int,input().split())
    roads[i].append((a,b))
    roads[i].append((c,d))

    if i==1:
        if a<=K:
            dp[i][a] = b

        if c<=K:
            dp[i][c] = max(dp[i][c],d)

for i in range(2,N+1):
    a,b = roads[i][0]
    c,d = roads[i][1]

    for j in range(K,0,-1):
        if j-a >= 1 and dp[i-1][j-a] > 0:
            dp[i][j] = max(dp[i][j],dp[i-1][j-a]+b)

        if j-c >= 1 and dp[i-1][j-c] > 0:
            dp[i][j] = max(dp[i][j],dp[i-1][j-c]+d)

print(max(dp[N]))
