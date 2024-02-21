import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
array = []
dp = [[0]*N for _ in range(N)]

for _ in range(N):
    array.append(int(input()))

for i in range(N):
    dp[i][i] = array[i]

def recursive_dp(left,right,cnt):
    if left == right:
        return dp[left][right]*cnt
    if dp[left][right]:
        return dp[left][right]

    dp[left][right] = max(dp[left][left]*cnt + recursive_dp(left+1,right,cnt+1),
                          dp[right][right]*cnt + recursive_dp(left,right-1,cnt+1))

    return dp[left][right]

recursive_dp(0,N-1,1)

print(dp[0][N-1])
