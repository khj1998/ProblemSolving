import sys
input = sys.stdin.readline
from collections import defaultdict

N,K = map(int,input().split())
dx,dy = [0,0,-1,1],[1,-1,0,0]
ans = 1
direc_dic = {}
axis_dic = defaultdict(list)
chess = []
horse = [[[] for _ in range(N)] for _ in range(N)]
can_end = False

for _ in range(N):
    chess.append(list(map(int,input().split())))

for i in range(K):
    x,y,direc = map(int,input().split())
    horse[x-1][y-1].append(i)
    axis_dic[i] = [x-1,y-1]
    direc_dic[i] = direc-1

def change_direc(direc):
    if direc <= 1:
        return (direc + 1) % 2
    elif direc == 2:
        return 3
    else:
        return 2

def change_position(num,x,y,px,py):
    idx = horse[x][y].index(num)
    temp = horse[x][y][idx:]

    while horse[x][y]:
        data = horse[x][y].pop()
        axis_dic[data] = [px,py]

        if data == num:
            break

    if chess[px][py] == 1:
        temp.reverse()

    for x in temp:
        horse[px][py].append(x)

def check_end():
    can_end = False

    for i in range(N):
        for j in range(N):
            if len(horse[i][j]) >= 4:
                can_end = True

    return can_end

while True:
    for i in range(K):
        num = i
        x,y = axis_dic[i]
        direc = direc_dic[num]
        px,py = x+dx[direc],y+dy[direc]

        if 0<=px<N and 0<=py<N:
            if chess[px][py] == 2:
                direc = change_direc(direc)
                direc_dic[num] = direc
                px,py = x+dx[direc],y+dy[direc]

                if 0<=px<N and 0<=py<N:
                    if chess[px][py] != 2:
                        change_position(num, x, y, px, py)
            else:
                change_position(num,x,y,px,py)
            can_end = check_end()
        else:
            direc = change_direc(direc)
            direc_dic[num] = direc
            px,py = x+dx[direc],y+dy[direc]

            if chess[px][py] != 2:
                change_position(num,x,y,px,py)
            can_end = check_end()

        if can_end:
            break

    if can_end:
        break

    ans += 1

    if ans > 1000:
        break

if ans > 1000 or not can_end:
    print(-1)
else:
    print(ans)
