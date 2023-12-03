import sys
input = sys.stdin.readline

N = int(input())
INF = int(1e9)
array = list(map(int,input().split()))
dp = [INF] * N
dp[0] = 0

# 한번 쓸 최대힘은 K, 이전에 갱신된 힘보다 작아도, 전체적으로 따졌을 때 가장 큰 힘의 값을 체크해야함.
for i in range(1,N):
    for j in range(0,i):
        K = max(dp[j],(i-j)*(1 + abs(array[j]-array[i])))
        dp[i] = min(dp[i],K)

print(dp[-1])