import sys
input=sys.stdin.readline
INF=int(1e9)

# 동전의 가치 종류 n, 총합 k원
n,k=map(int,input().split())
coin_types=[]
for _ in range(n):
    a=int(input())
    if a not in coin_types:
        coin_types.append(a)

dp=[INF]*(k+1)
dp[0]=0

for i in range(len(coin_types)):
    coin_value=coin_types[i]
    for j in range(coin_value,k+1):
        dp[j]=min(dp[j],dp[j-coin_value]+1)

if dp[k]==INF:
    print(-1)
else:
    print(dp[k])