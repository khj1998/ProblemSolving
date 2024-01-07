import sys
input = sys.stdin.readline
from collections import deque

if __name__=="__main__":
    R,C = map(int,input().split())
    q,q2 = deque(),deque()
    INF = int(1e7)
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    forest = []
    water_graph = [[INF]*C for _ in range(R)]
    animal_graph = [[INF]*C for _ in range(R)]
    end_x,end_y = 0,0

    for _ in range(R):
        forest.append(str(input()).rstrip())

    for i in range(R):
        for j in range(C):
            if forest[i][j] == '*':
                water_graph[i][j] = 0
                q.append((i,j))

            if forest[i][j] == 'S':
                animal_graph[i][j] = 0
                q2.append((i,j))

            if forest[i][j] == 'D':
                end_x,end_y = i,j

    while q:
        x,y = q.popleft()

        for i in range(4):
            px,py = x+dx[i],y+dy[i]

            if 0<=px<R and 0<=py<C and forest[px][py] == '.' and forest[px][py] != 'D':
                if water_graph[px][py] > water_graph[x][y] + 1:
                    water_graph[px][py] =  water_graph[x][y] + 1
                    q.append((px,py))

    while q2:
        x,y = q2.popleft()

        for i in range(4):
            px,py = x+dx[i],y+dy[i]

            if 0<=px<R and 0<=py<C and forest[px][py] != 'X':
                next_cost = animal_graph[x][y] + 1

                if animal_graph[px][py] > next_cost and animal_graph[x][y] + 2 <= water_graph[px][py]:
                    animal_graph[px][py] = next_cost
                    q2.append((px,py))

    if animal_graph[end_x][end_y] == INF:
        print('KAKTUS')
    else:
        print(animal_graph[end_x][end_y] )
