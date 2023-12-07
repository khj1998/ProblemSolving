import sys
input = sys.stdin.readline
from itertools import combinations
from collections import defaultdict
from collections import deque

N,M = map(int,input().split())
ans = 0
dx,dy = [-1,1,0,0],[0,0,-1,1]
check = [[False]*M for _ in range(N)]
board = []
axis_list = []
group = defaultdict(list)
group_total_axis = defaultdict(int)

def check_group(x,y,cnt):
    q = deque()
    q.append((x,y))
    check[x][y] = True
    total_group_cnt = 1
    group[cnt] = []

    while q:
        x,y = q.popleft()

        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]

            if 0<=px<N and 0<=py<M:
                if board[px][py] == 2 and not check[px][py]:
                    check[px][py] = True
                    total_group_cnt += 1
                    q.append((px,py))
                elif board[px][py] == 0 and [px,py] not in group[cnt]:
                    group[cnt].append([px,py])

    group_total_axis[cnt] = total_group_cnt

def is_escapable(group_axis):
    cnt = 0
    escapable_cnt = 0

    for x,y in group_axis:
        if board[x][y] == 0:
            escapable_cnt += 1

    return cnt != escapable_cnt

for _ in range(N):
    board.append(list(map(int,input().split())))

cnt = 1

for i in range(N):
    for j in range(M):
        if board[i][j] == 2 and not check[i][j]:
            check_group(i,j,cnt)
            cnt+=1

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            axis_list.append([i,j])

axis_list = list(combinations(axis_list,2))

for axis in axis_list:
    x1,y1 = axis[0]
    x2, y2 = axis[1]
    board[x1][y1],board[x2][y2] = 1,1
    count = 0

    for key in group.keys():
        if not is_escapable(group[key]):
            count += group_total_axis[key]

    ans = max(ans, count)
    board[x1][y1], board[x2][y2] = 0,0

print(ans)