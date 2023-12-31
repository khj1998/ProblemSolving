import sys
input = sys.stdin.readline
from collections import deque

M,N,K = map(int,input().split())
ans = []
dx,dy = [-1,1,0,0],[0,0,-1,1]
rectangle = [[False]*N for _ in range(M)]

for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())

    for i in range(y1,y2):
        for j in range(x1,x2):
            rectangle[i][j] = True

def find_area(x,y):
    q = deque()
    count = 0
    rectangle[x][y] = True
    q.append((x,y))

    while q:
        x,y = q.popleft()
        count += 1

        for i in range(4):
            px,py = x+dx[i],y+dy[i]

            if 0<=px<M and 0<=py<N and not rectangle[px][py]:
                rectangle[px][py] = True
                q.append((px,py))

    ans.append(count)

for i in range(M):
    for j in range(N):
        if not rectangle[i][j]:
            find_area(i,j)

ans.sort()
print(len(ans))

for i in ans:
    print(i,end=" ")
