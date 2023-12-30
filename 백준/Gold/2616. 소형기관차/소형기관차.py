import sys
input = sys.stdin.readline

N = int(input())
array = [0] + list(map(int,input().split()))
dp = [[0]*(N+1) for _ in range(4)]

for i in range(2,N+1):
    array[i] += array[i-1]

M = int(input())

for i in range(1,4):
    for j in range(M,N+1):
        dp[i][j] = max(dp[i][j-1],dp[i-1][j-M] + array[j] - array[j-M])

print(dp[3][N])
