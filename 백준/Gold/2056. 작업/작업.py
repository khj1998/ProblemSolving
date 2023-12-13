import sys
input=sys.stdin.readline
from collections import deque

N=int(input())
in_degree=[0]*(N+1)
dp=[0]*(N+1)
ans=0
time=[0]*(N+1)
graph=[[] for _ in range(N+1)]
q=deque()

for i in range(1,N+1):
    info=list(map(int,input().split()))
    time[i]=info[0]
    num=info[1]
    if num==0:
        continue
    else:
        in_degree[i] = info[1]
        for j in range(2,2+num):
            graph[info[j]].append(i)

for i in range(1,N+1):
    if in_degree[i]==0:
        dp[i]=time[i]
        q.append(i)

while q:
    x=q.popleft()

    for y in graph[x]:
        if in_degree[y]>0:
            dp[y]=max(dp[y],dp[x]+time[y])
            in_degree[y]-=1
        if not in_degree[y]:
            q.append(y)

print(max(dp))