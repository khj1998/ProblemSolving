import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
from copy import deepcopy

N,M = map(int,input().split())
answer = -1
virus_map = []
wall_cases = []
dx,dy = [-1,1,0,0],[0,0,-1,1]

for _ in range(N):
    virus_map.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if virus_map[i][j] == 0:
            wall_cases.append((i,j))

wall_cases = list(combinations(wall_cases,3))

def get_safe_area(case):
    cnt = 0
    q = deque()
    temp_map = deepcopy(virus_map)

    for x,y in case:
        temp_map[x][y] = 1

    for x in range(N):
        for y in range(M):
            if temp_map[x][y] == 2:
                q.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]

            if 0<=px<N and 0<=py<M:
                if temp_map[px][py] == 0:
                    temp_map[px][py] = 2
                    q.append((px,py))

    for x in range(N):
        for y in range(M):
            if temp_map[x][y] == 0:
                cnt+=1

    return cnt

for case in wall_cases:
    answer = max(answer,get_safe_area(case))

print(answer)