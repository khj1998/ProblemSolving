import sys
input=sys.stdin.readline

n,k=map(int,input().split())
dp=[0]*(k+1)
dp[0]=1
coin_type=[]
for _ in range(n):
    a=int(input())
    coin_type.append(a)

for i in range(n):
    value=coin_type[i]

    for j in range(value,k+1):
        dp[j]+=dp[j-value]

print(dp[k])