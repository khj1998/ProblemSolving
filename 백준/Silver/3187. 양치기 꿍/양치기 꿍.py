import sys
input = sys.stdin.readline
from collections import deque

R,C = map(int,input().split())
dx,dy = [-1,1,0,0],[0,0,-1,1]
answer = [0,0]
check = [[False]*C for _ in range(R)]
graph = []

def bfs(x,y):
    q = deque()
    q.append((x,y))
    check[x][y] = True
    ans = [0,0]

    while q:
        x,y = q.popleft()

        if graph[x][y] == 'k':
            ans[0] += 1
        elif graph[x][y] == 'v':
            ans[1] += 1

        for i in range(4):
            px,py = x+dx[i],y+dy[i]

            if 0<=px<R and 0<=py<C and not check[px][py]:
                if not check[px][py] and graph[px][py] != '#':
                    check[px][py] = True
                    q.append((px,py))

    if ans[0] > ans[1]:
        ans = [ans[0],0]
    else:
        ans = [0,ans[1]]

    return ans

for _ in range(R):
    graph.append(str(input()).rstrip())

for i in range(R):
    for j in range(C):
        if not check[i][j] and graph[i][j] in ['v','k']:
            ans = bfs(i,j)
            answer[0] += ans[0]
            answer[1] += ans[1]

for i in answer:
    print(i,end=" ")
