import sys
input = sys.stdin.readline

N = int(input())
array = [0] + list(map(int,input().split()))
dp = [0] * (N+1)
dp[1] = array[1]

for i in range(2,N+1):
    temp = 0
    for j in range(1,len(array)):
        if j > i:
            break
        temp = max(temp,array[j] + dp[i-j])
    dp[i] = temp

print(dp[N])