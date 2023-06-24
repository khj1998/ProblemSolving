import sys
import heapq
from collections import deque

dx,dy = [-1,1,0,0],[0,0,-1,1]

def bfs(x,y,key):
    q = deque()
    q.append((x,y))
    check[x][y] = True
    color = graph[x][y]

    while q:
        x,y = q.popleft()

        for i in range(4):
            px = x+dx[i]
            py = y+dy[i]

            if 0<=px<regions and 0<=py<regions and not check[px][py]:
                if key == 0:
                    if color == graph[px][py]:
                        check[px][py] = True
                        q.append((px,py))
                else:
                    is_same = False
                    if color == "R":
                        if color == graph[px][py] or graph[px][py] == "G":
                            is_same = True
                    elif color == "G":
                        if color == graph[px][py] or graph[px][py] == "R":
                            is_same = True
                    else:
                        if color == graph[px][py]:
                            is_same = True

                    if is_same:
                        check[px][py] = True
                        q.append((px, py))

if __name__ =="__main__":
    regions = int(input())
    check = [[False]*regions for _ in range(regions)]
    graph = []
    normal,non_normal = 0,0

    for _ in range(regions):
        graph.append(str(input().rstrip()))

    for i in range(regions):
        for j in range(regions):
            if not check[i][j]:
                bfs(i,j,0)
                normal+=1

    check = [[False]*regions for _ in range(regions)]

    for i in range(regions):
        for j in range(regions):
            if not check[i][j]:
                bfs(i,j,1)
                non_normal+=1

    print(str(normal)+" "+str(non_normal))