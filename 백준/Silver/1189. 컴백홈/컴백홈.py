import sys
input = sys.stdin.readline

#집 위치 0,C-1
ans = 0
R,C,K = map(int,input().split())
dx,dy = [-1,1,0,0],[0,0,-1,1]
check = [[False]*C for _ in range(R)]
graph = []

for _ in range(R):
    graph.append(str(input()).rstrip())

def dfs(x,y,cnt):
    global ans

    check[x][y] = True

    if x == 0 and y == C-1 and cnt == K:
        ans += 1
        check[x][y] = False
        return False
    elif cnt > K:
        return False

    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]

        if 0<=px<R and 0<=py<C and not check[px][py] and graph[px][py] != 'T':
            check[px][py] = dfs(px,py,cnt+1)

dfs(R-1,0,1)

print(ans)
