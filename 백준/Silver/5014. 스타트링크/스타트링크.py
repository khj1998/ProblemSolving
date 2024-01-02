import sys
input = sys.stdin.readline
from collections import deque

# 총 F층, 링크가 있는 곳 위치 G, 현재 위치 S층, U 위로 몇층, D 아래로 몇층
F,S,G,U,D = map(int,input().split())
q = deque()
INF = int(1e8)
q.append((S,0))
start_link = [INF]*(F+1)
start_link[S] = 0

while q:
    now,cnt = q.popleft()

    if D > 0 and  now - D >= 1 and start_link[now-D] > cnt+1:
        start_link[now-D] = cnt + 1
        q.append((now-D,cnt+1))

    if U > 0 and now + U <= F and start_link[now+U] > cnt+1:
        start_link[now + U] = cnt + 1
        q.append((now+U,cnt+1))

if start_link[G] == INF:
    print('use the stairs')
else:
    print(start_link[G])
