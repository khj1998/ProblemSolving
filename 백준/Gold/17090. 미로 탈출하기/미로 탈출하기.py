import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())
ans = 0
graph = []
dx,dy = [-1,0,1,0],[0,1,0,-1]
check_capable = [[False]*M for _ in range(N)]
check = [[False]*M for _ in range(N)]

for _ in range(N):
    graph.append(str(input()).rstrip())

def dfs(x,y,start_x,start_y,path):
    if graph[x][y] == 'U':
        x, y = x - 1, y
    elif graph[x][y] == 'R':
        x, y = x, y+1
    elif graph[x][y] == 'D':
        x, y = x+1, y
    else:
        x, y = x, y-1

    if 0<=x<N and 0<=y<M:
        if (x,y) in path.keys():
            check_capable[start_x][start_y] = False
            check_capable[x][y] = False
            return False

        if check_capable[x][y]:
            check_capable[start_x][start_y] = True
            check_capable[x][y] = True
            return True

        path[(x,y)] = 1
        check_capable[x][y] = dfs(x,y,start_x,start_y,path)
        return check_capable[x][y]
    else:
        check_capable[start_x][start_y]= True
        return True

for i in range(N):
    for j in range(M):
        if not check[i][j]:
            path = {}
            path[(i,j)] = 1
            dfs(i,j,i,j,path)

for i in range(N):
    for j in range(M):
        if check_capable[i][j]:
            ans += 1

print(ans)
