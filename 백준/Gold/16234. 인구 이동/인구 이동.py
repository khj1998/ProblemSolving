import sys
sys.setrecursionlimit(10**4)
from collections import deque
input=sys.stdin.readline

n,l,r=map(int,input().split())
graph=[]
days=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for _ in range(n):
    graph.append(list(map(int,input().split())))

def bfs(x,y):
    global count
    q=deque()
    population=graph[x][y]
    kingdom = []
    q.append((x,y))
    check[x][y] = True

    while q:
        x,y=q.popleft()
        kingdom.append((x,y))
        for i in range(4):
            px=x+dx[i]
            py=y+dy[i]
            if 0<=px<n and 0<=py<n:
                if l<=abs(graph[x][y]-graph[px][py])<=r and not check[px][py]:
                    q.append((px,py))
                    check[px][py] = True
                    population+=graph[px][py]

    countries=len(kingdom)
    count=max(count,countries)
    if countries>1:
        for x,y in kingdom:
            graph[x][y]=population//countries


while 1:
    check = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                bfs(i,j)

    if count<=1:
        print(days)
        break
    days+=1