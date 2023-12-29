import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N = int(input())
dp = [[0]*N for _ in range(N)]
rice_value = []

for _ in range(N):
    rice_value.append(int(input()))

def get_dp(start,end,cnt):
    if start > end:
        return 0

    if dp[start][end]:
        return dp[start][end]

    dp[start][end] = max(cnt*rice_value[start] + get_dp(start+1,end,cnt+1),
                         cnt*rice_value[end] + get_dp(start,end-1,cnt+1))

    return dp[start][end]

get_dp(0,N-1,1)

print(dp[0][N-1])
