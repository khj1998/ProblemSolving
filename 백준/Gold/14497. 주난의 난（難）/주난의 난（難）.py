import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
x1,y1,x2,y2 = map(int,input().split())
dx,dy = [-1,1,0,0],[0,0,-1,1]
space_temp = []
space = [[] for _ in range(N)]
ans = 0

for _ in range(N):
    space_temp.append(str(input()).rstrip())

for i in range(N):
    for j in range(M):
        if space_temp[i][j] == '1':
            space[i].append(1)
        elif space_temp[i][j] == '0':
            space[i].append(0)
        elif space_temp[i][j] == '#':
            space[i].append(2)
        else:
            space[i].append(3)

def bfs(x,y):
    q = deque()
    q.append((x,y))
    check = [[False]*M for _ in range(N)]
    check[x][y] = True

    while q:
        x,y = q.popleft()

        for i in range(4):
            px,py = x+dx[i],y+dy[i]

            if 0<=px<N and 0<=py<M and not check[px][py]:
                if space[px][py] == 2:
                    return True

                if space[px][py] == 1:
                    check[px][py] = True
                    space[px][py] = 0
                else:
                    check[px][py] = True
                    q.append((px,py))

    return False

while True:
    ans += 1
    result = bfs(x1-1,y1-1)
    if result:
        break

print(ans)
