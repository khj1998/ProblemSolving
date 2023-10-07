import sys
input=sys.stdin.readline
from collections import deque

INF=int(1e9)
R,C=map(int,input().split())
graph=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(R):
    graph.append(list(input().strip()))

jihun_map=[[INF]*C for _ in range(R)]
fire_map=[[INF]*C for _ in range(R)]
start=[]
f_start=[]

for i in range(R):
    for j in range(C):
        if graph[i][j]=='J':
            start.append((i,j))
        elif graph[i][j]=='F':
            f_start.append((i,j))

def jihun_bfs():
    q=deque()
    q.append((start[0][0],start[0][1]))
    jihun_map[start[0][0]][start[0][1]]=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            px=x+dx[i]
            py=y+dy[i]

            if 0<=px<R and 0<=py<C:
                if jihun_map[px][py]>jihun_map[x][y]+1 and graph[px][py]=='.':
                    jihun_map[px][py]=jihun_map[x][y]+1
                    q.append((px,py))

def fire_bfs():
    q = deque()
    for x,y in f_start:
        fire_map[x][y]=1
        q.append((x,y))

    while q:
        x,y=q.popleft()
        for i in range(4):
            px=x+dx[i]
            py=y+dy[i]

            if 0<=px<R and 0<=py<C:
                if fire_map[px][py]>fire_map[x][y]+1 and graph[px][py]=='.':
                    fire_map[px][py]=fire_map[x][y]+1
                    q.append((px,py))

jihun_bfs()
fire_bfs()
jihun_end=INF
fire_end=INF

def is_escape():
    ans=INF
    # 맨위,맨 아래, 맨 오른쪽,맨 왼쪽
    for i in range(C):
        if jihun_map[0][i]<fire_map[0][i]:
            ans=min(ans,jihun_map[0][i])

    for i in range(C):
        if jihun_map[R-1][i]<fire_map[R-1][i]:
            ans=min(ans,jihun_map[R-1][i])

    for i in range(R):
        if jihun_map[i][0]<fire_map[i][0]:
            ans=min(ans,jihun_map[i][0])

    for i in range(R):
        if jihun_map[i][C-1]<fire_map[i][C-1]:
            ans=min(ans,jihun_map[i][C-1])

    if ans==INF:
        print("IMPOSSIBLE")
    else:
        print(ans)

is_escape()