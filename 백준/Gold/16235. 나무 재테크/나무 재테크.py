import sys
input = sys.stdin.readline
from collections import deque

N,M,K = map(int,input().split())
ans = 0
array = []
nutrient_map = [[5]*N for _ in range(N)]
dx,dy = [-1,1,0,0,-1,1,-1,1],[0,0,-1,1,-1,-1,1,1]
live_tree = [[deque() for _ in range(N)] for _ in range(N)]
dead_tree = []

for _ in range(N):
    array.append(list(map(int,input().split())))

for _ in range(M):
    x,y,age = map(int,input().split())
    live_tree[x-1][y-1].append(age)

for _ in range(K):
    for i in range(N):
        for j in range(N):
            len_ = len(live_tree[i][j])

            for k in range(len_):
                if nutrient_map[i][j] >= live_tree[i][j][k]:
                    nutrient_map[i][j] -= live_tree[i][j][k]
                    live_tree[i][j][k] += 1
                else:
                    for _ in range(k,len_):
                        dead_tree.append((i,j,live_tree[i][j].pop()))
                    break

    while dead_tree:
        x,y,age = dead_tree.pop()
        nutrient_map[x][y] += age // 2

    for i in range(N):
        for j in range(N):
            len_ = len(live_tree[i][j])

            for k in range(len_):
                if live_tree[i][j][k]%5==0:

                    for g in range(8):
                        px,py = i+dx[g],j+dy[g]

                        if 0<=px<N and 0<=py<N:
                            live_tree[px][py].appendleft(1)

            nutrient_map[i][j] += array[i][j]

for i in range(N):
    for j in range(N):
        ans += len(live_tree[i][j])

print(ans)
