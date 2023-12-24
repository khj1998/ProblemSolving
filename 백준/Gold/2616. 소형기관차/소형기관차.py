import sys
input = sys.stdin.readline

n = int(input())
array = [0] + list(map(int,input().split()))
m = int(input())
array_sum = [0]*(n+1)
dp = [[0]*(n+1) for _ in range(4)]

for i in range(1,n+1):
    array_sum[i] = array[i] + array_sum[i-1]

for i in range(1,4):
    for j in range(m,n+1):
        dp[i][j] = max(dp[i][j-1],dp[i-1][j-m]+array_sum[j]-array_sum[j-m])

print(dp[3][n])