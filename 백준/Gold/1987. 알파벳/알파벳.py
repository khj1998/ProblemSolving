import sys
input = sys.stdin.readline

R,C = map(int,input().split())
dx,dy = [-1,1,0,0],[0,0,-1,1]
graph = []
ans = [1]

for _ in range(R):
    graph.append(str(input()).rstrip())

def dfs(x,y,path,cnt):
    for i in range(4):
        px,py = x+dx[i],y+dy[i]

        if 0<=px<R and 0<=py<C:
            if graph[px][py] not in path:
                dfs(px,py,path+graph[px][py],cnt+1)
            else:
                ans[0] = max(ans[0],cnt)

dfs(0,0,graph[0][0],1)
print(ans[0])

