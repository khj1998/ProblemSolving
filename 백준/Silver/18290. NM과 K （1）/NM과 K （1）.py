import sys
input = sys.stdin.readline
from itertools import combinations

N,M,K = map(int,input().split())
dx,dy =  [-1,1,0,0],[0,0,-1,1]
ans = -int(1e8)
axis_list = []
grid = []

for _ in range(N):
    row = list(map(int,input().split()))
    grid.append(row)

for i in range(N):
    for j in range(M):
        axis_list.append((i,j))

sum_list = list(combinations(axis_list,K))

for l in sum_list:
    is_possible = True
    temp = 0

    for x,y in l:
        for i in range(4):
            px = x+dx[i]
            py = y+dy[i]

            if (px,py) in l:
                is_possible = False
                break

        if is_possible:
            temp += grid[x][y]
        else:
            break

    if not is_possible:
        continue

    ans = max(ans,temp)

print(ans)