import sys
input = sys.stdin.readline
from collections import deque

N,K = map(int,input().split())
INF = int(1e8)
dp = [INF]*200001

q = deque()
dp[N] = 0
q.append((N,0))

while q:
    now,time = q.popleft()

    if now - 1 >= 0 and dp[now-1] > time+1:
        dp[now-1] = time + 1
        q.append((now-1,time+1))

    if now + 1 <= 200000 and dp[now+1] > time+1:
        dp[now+1] = time + 1
        q.append((now+1,time+1))

    if now*2 <= 200000 and dp[now*2] > time:
        dp[now*2] = time
        q.append((now*2,time))

print(dp[K])
