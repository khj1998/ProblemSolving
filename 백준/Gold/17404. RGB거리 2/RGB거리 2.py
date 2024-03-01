import sys
input=sys.stdin.readline
INF=int(1e9)

n=int(input())
array=[]
for _ in range(n):
    a,b,c=map(int,input().split())
    array.append([a,b,c])

dp=[[0]*3 for _ in range(n)]
result=INF

for i in range(3):
    for j in range(3):
        if j==i:
            dp[0][j]=array[0][j]
        else:
            dp[0][j]=INF

    for k in range(1,n):
        dp[k][0]=array[k][0]+min(dp[k-1][1],dp[k-1][2])
        dp[k][1]=array[k][1]+min(dp[k-1][0],dp[k-1][2])
        dp[k][2]=array[k][2]+min(dp[k-1][0],dp[k-1][1])

    for k in range(3):
        if i==k:
            continue
        result=min(result,dp[n-1][k])

print(result)