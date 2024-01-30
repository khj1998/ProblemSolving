import sys
input = sys.stdin.readline

R,C,T = map(int,input().split())
dx,dy = [-1,1,0,0],[0,0,-1,1]
filter_axis = []
graph = []
ans = 0

for _ in range(R):
    graph.append(list(map(int,input().split())))

for i in range(R):
    if graph[i][0] == -1:
        filter_axis.append((i,0))
        filter_axis.append((i++1,0))
        break

def spread(x,y):
    cnt = 0
    amount = graph[x][y]//5

    for i in range(4):
        px,py = x+dx[i],y+dy[i]

        if 0<=px<R and 0<=py<C and graph[px][py]!=-1:
            spread_graph[px][py] += amount
            cnt+=1

    graph[x][y] -= (amount*cnt)

def rotate():
    upper_x,upper_y = filter_axis[0][0]-1,filter_axis[0][1]
    down_x,down_y = filter_axis[1][0]+1,filter_axis[1][1]

    while upper_x-1 >= 0:
        graph[upper_x][upper_y] = graph[upper_x-1][upper_y]
        upper_x-=1

    while upper_y+1 < C:
        graph[upper_x][upper_y] = graph[upper_x][upper_y+1]
        upper_y+=1

    while upper_x+1 <= filter_axis[0][0]:
        graph[upper_x][upper_y] = graph[upper_x+1][upper_y]
        upper_x+=1

    while upper_y-1 >= 1:
        graph[upper_x][upper_y] = graph[upper_x][upper_y-1]
        upper_y-=1

    while down_x+1 < R:
        graph[down_x][down_y] = graph[down_x+1][down_y]
        down_x+=1

    while down_y+1 < C:
        graph[down_x][down_y] = graph[down_x][down_y+1]
        down_y+=1

    while down_x-1 >= filter_axis[1][0]:
        graph[down_x][down_y] = graph[down_x-1][down_y]
        down_x-=1

    while down_y-1 >= 1:
        graph[down_x][down_y] = graph[down_x][down_y-1]
        down_y-=1

    graph[filter_axis[0][0]][filter_axis[0][1]+1] = 0
    graph[filter_axis[1][0]][filter_axis[1][1] + 1] = 0

for _ in range(T):
    spread_graph = [[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                spread(i,j)

    for i in range(R):
        for j in range(C):
            graph[i][j] += spread_graph[i][j]

    rotate()

for i in range(R):
    for j in range(C):
        if graph[i][j] > 0:
            ans += graph[i][j]

print(ans)
