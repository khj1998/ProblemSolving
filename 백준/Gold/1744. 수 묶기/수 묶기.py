import sys
input = sys.stdin.readline

N = int(input())
array = []
dp = [[0]*(N+1) for _ in range(2)]

for _ in range(N):
    array.append(int(input()))

array.sort(reverse=True)
array = [0] + array
dp[0][1],dp[1][1] = array[1],array[1]

for i in range(2,N+1):
    dp[0][i] = max(dp[0][i-1]+array[i],dp[1][i-1]+array[i])
    dp[1][i] = max(array[i]*array[i-1]+dp[0][i-2],array[i]*array[i-1]+dp[1][i-2])

print(max(dp[0][N],dp[1][N]))
