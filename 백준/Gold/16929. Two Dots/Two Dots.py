import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
board = []
is_cycle = False
dx,dy = [-1,1,0,0],[0,0,-1,1]
check = [[False]*M for _ in range(N)]
edges = []

for _ in range(N):
    board.append(str(input()).rstrip())

def bfs(x,y,color):
    q = deque()
    node_check = [(x,y)]
    edge_cnt = 0
    q.append((x,y))
    check[x][y] = True

    while q:
        x,y = q.popleft()

        for i in range(4):
            px,py = x+dx[i],y+dy[i]

            if 0<=px<N and 0<=py<M and board[px][py] == color:
                if (x,y,px,py) not in edges:

                    if (px,py) not in node_check:
                        node_check.append((px,py))

                    edges.append((x,y,px,py))
                    edges.append((px,py,x,y))
                    edge_cnt += 1
                    q.append((px,py))
                    check[px][py] = True

    node_cnt = len(node_check)

    return node_cnt <= edge_cnt

for i in range(N):
    for j in range(M):
        if not check[i][j] and bfs(i,j,board[i][j]):
            is_cycle = True

    if is_cycle:
        break

if is_cycle:
    print('Yes')
else:
    print('No')
