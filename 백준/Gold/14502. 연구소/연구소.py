import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy
from itertools import combinations

dx,dy = [-1,1,0,0],[0,0,-1,1]

def spread(v_q):
    ans = 0

    while v_q:
        x,y = v_q.popleft()
        for i in range(4):
            px = x+dx[i]
            py = y+dy[i]

            if 0<=px<N and 0<=py<M:
                if temp_graph[px][py] == 0:
                    temp_graph[px][py] = 1
                    v_q.append((px,py))

    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 0:
                ans+=1
    return ans

if __name__ =="__main__":
    N,M = map(int,input().split())
    wall = []
    graph = []
    virsus = []
    virus_q = deque()
    answer = -1

    for _ in range(N):
        graph.append(list(map(int,input().split())))

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                wall.append((i,j))
            if graph[i][j] == 2:
                virus_q.append((i,j))

    walls = list(combinations(wall,3))

    for w in walls:
        temp_graph = deepcopy(graph)
        temp_graph[w[0][0]][w[0][1]] = 1
        temp_graph[w[1][0]][w[1][1]] = 1
        temp_graph[w[2][0]][w[2][1]] = 1

        temp_q = deepcopy(virus_q)
        answer = max(answer,spread(temp_q))

    print(answer)