import sys
input=sys.stdin.readline
from collections import deque
# 14428 수열과 쿼리 16 풀기
INF=int(1e6)

T=int(input())
dx,dy=[-1,1,0,0],[0,0,-1,1]

def sanggun_bfs(start):
    start_x,start_y=start
    q=deque()
    q.append((start_x,start_y))
    dp1[start_x][start_y]=0

    while q:
        x,y=q.popleft()
        for i in range(4):
            px=x+dx[i]
            py=y+dy[i]
            if 0<=px<h and 0<=py<w and graph[px][py]!='#':
                if dp1[px][py]>dp1[x][y]+1:
                    dp1[px][py]=dp1[x][y]+1
                    q.append((px,py))

def fire_bfs(fire):
    q=deque()
    for x,y in fire:
        q.append((x,y))
        dp2[x][y]=0

    while q:
        x,y=q.popleft()
        for i in range(4):
            px=x+dx[i]
            py=y+dy[i]
            if 0<=px<h and 0<=py<w and graph[px][py]!='#':
                if dp2[px][py]>dp2[x][y]+1:
                    dp2[px][py]=dp2[x][y]+1
                    q.append((px,py))


for _ in range(T):
    ans = INF
    w, h = map(int, input().split())
    start, graph, fire = [], [], []
    for _ in range(h):
        graph.append(input())
    dp1 = [[INF] * w for _ in range(h)]
    dp2 = [[INF] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@':
                start = [i, j]
            elif graph[i][j] == '*':
                fire.append((i, j))

    sanggun_bfs(start)
    fire_bfs(fire)

    for i in range(w):
        if dp1[0][i] < dp2[0][i]:
            ans = min(ans, dp1[0][i])

    for i in range(w):
        if dp1[h - 1][i] < dp2[h - 1][i]:
            ans = min(ans, dp1[h - 1][i])

    for i in range(h):
        if dp1[i][0] < dp2[i][0]:
            ans = min(ans, dp1[i][0])

    for i in range(h):
        if dp1[i][w - 1] < dp2[i][w - 1]:
            ans = min(ans, dp1[i][w - 1])

    if ans == INF:
        print("IMPOSSIBLE")
    else:
        print(ans + 1)