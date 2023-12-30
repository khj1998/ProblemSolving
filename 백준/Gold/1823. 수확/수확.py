import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())
dp = [[0]*N for _ in range(N)]
values = []

for _ in range(N):
    values.append(int(input()))

def recursive(left,right,cnt):
    if right < left:
        return 0
    elif dp[left][right]:
        return dp[left][right]

    dp[left][right] = max(cnt*values[left] + recursive(left+1,right,cnt+1),
                          cnt*values[right] + recursive(left,right-1,cnt+1))

    return dp[left][right]

recursive(0,N-1,1)

print(dp[0][N-1])
