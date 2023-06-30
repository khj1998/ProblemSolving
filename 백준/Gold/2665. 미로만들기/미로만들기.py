import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    check = [[-1] * n for _ in range(n)]

    q = deque()
    q.append((0,0))
    check[0][0] = 0

    while q:
        x,y  = q.popleft()
        for i in range(4):
            px = x+dx[i]
            py = y+dy[i]

            if 0<=px<n and 0<=py<n:
                if graph[px][py] == '1':
                    if check[px][py] == -1:
                        check[px][py] = check[x][y]
                        q.append((px,py))
                    elif check[px][py] > check[x][y]:
                        check[px][py] = check[x][y]
                        q.append((px,py))
                else:
                    if check[px][py] == -1:
                        check[px][py] = check[x][y] + 1
                        q.append((px,py))
                    else:
                        if check[px][py] > check[x][y]+1:
                            check[px][py] = check[x][y] + 1
                            q.append((px, py))

    return check[n-1][n-1]

if __name__ =="__main__":
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    n = int(input())
    graph = []

    for _ in range(n):
        graph.append(list(map(str,input().rstrip())))

    print(bfs())