import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
time = [0] * (N+1)
time_dp = [0] * (N+1)
degree = [0] * (N+1)
now_work = deque()
topology_graph = [[] for _ in range(N+1)]

for i in range(1,N+1):
    jobs = list(map(int,input().split()))
    time[i] = jobs[0]
    time_dp[i] = jobs[0]

    if jobs[1] > 0:
        for j in range(2,len(jobs)):
            degree[i]+=1
            topology_graph[jobs[j]].append(i)

for i in range(1,N+1):
    if degree[i] == 0:
        now_work.append(i)

while now_work:
    x = now_work.popleft()

    for y in topology_graph[x]:
        degree[y] -= 1
        time_dp[y] = max(time_dp[y],time_dp[x] + time[y])
        if degree[y] == 0:
            now_work.append(y)

print(max(time_dp))