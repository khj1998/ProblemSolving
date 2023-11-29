import sys
input = sys.stdin.readline
import math

H,Y = map(int,input().split())
dp = [0] * (Y+1)
dp[0] = H

for i in range(1,Y+1):
    dp[i] = int(dp[i-1]*1.05)

    if i>=3:
        dp[i] = int(max(dp[i],dp[i-3]*1.2))

    if i>=5:
        dp[i] = int(max(dp[i],dp[i-5]*1.35))

print(dp[Y])