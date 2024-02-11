import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
INF = int(1e8)

N,M = map(int,input().split())
graph = []
dx,dy = [-1,1,0,0],[0,0,-1,1]
virus_list = []
virus_cnt = 0
ans = INF

for _ in range(N):
    graph.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus_list.append((i,j))
        if graph[i][j] != 1:
            virus_cnt += 1

virus_list = list(combinations(virus_list,M))

def solution(v_list):
    check = [[INF]*N for _ in range(N)]
    cnt = 0
    time = 0
    q = deque()

    for x,y in v_list:
        check[x][y] = 0
        cnt += 1
        q.append((x,y,0))

    while q:
        x,y,t = q.popleft()
        time = t

        for i in range(4):
            px,py = x+dx[i],y+dy[i]

            if 0<=px<N and 0<=py<N:
                if graph[px][py] != 1 and check[px][py] > check[x][y] + 1:
                    check[px][py] = check[x][y] + 1
                    cnt += 1
                    q.append((px,py,check[x][y]+1))

    if cnt == virus_cnt:
        return time
    else:
        return INF

for v_list in virus_list:
    ans = min(ans,solution(v_list))

if ans == INF:
    print(-1)
else:
    print(ans)
