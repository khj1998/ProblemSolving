import sys
input=sys.stdin.readline

n=int(input())
array=[]
for _ in range(n):
    a=int(input())
    array.append(a)
dp=[0]*n
if n>=1:
    dp[0]=array[0]
if n>=2:
    dp[1]=array[0]+array[1]
if n>=3:
    dp[2]=max(array[0],array[1])+array[2]
if n>=4:
    for i in range(3,n):
        dp[i]=max(array[i-1]+dp[i-3],dp[i-2])+array[i]

print(dp[-1])