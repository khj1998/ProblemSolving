import sys
input = sys.stdin.readline

N = int(input())
INF = int(1e9)
array = list(map(int,input().split()))
dp = [INF]*N
dp[0] = 0

for i in range(N):
    cnt = 1

    while cnt <= array[i] and i+cnt <= N-1:
        dp[i+cnt] = min(dp[i]+1,dp[i+cnt])
        cnt += 1

if dp[N-1] == INF:
    print(-1)
else:
    print(dp[N-1])
