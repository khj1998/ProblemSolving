import sys
input = sys.stdin.readline
from collections import defaultdict

R,C,M = map(int,input().split())
now_col = 0
ans = 0
max_row_move = R - 1
max_col_move = C - 1
shark_axis = [[[] for _ in range(C+1)] for _ in range(R+1)]
axis_dic = {}

for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    key = str(r)+" "+str(c)
    axis_dic[key] = 1
    shark_axis[r][c].append([r,c,s,d-1,z])

while now_col < C:
    now_col+=1
    next_axis_dic = {}
    next_shark_axis = [[[] for _ in range(C+1)] for _ in range(R+1)]

    for i in range(1,R+1):
        if shark_axis[i][now_col]:
            r,c,s,d,z = shark_axis[i][now_col][0]
            ans += z
            shark_axis[i][now_col].pop()
            break

    for key in axis_dic.keys():
        i,j = key.split(' ')
        i,j = int(i),int(j)
        for r,c,s,d,z in shark_axis[i][j]:
            if s == 0:
                key = str(r) +" "+ str(c)
                next_axis_dic[key] = 1
                next_shark_axis[r][c].append([r,c,s,d,z])
                continue
            if d == 0:
                diff = (r-1) - s

                if diff >= 0:
                    r -= s
                    key = str(r) +" "+ str(c)
                    next_axis_dic[key] = 1
                    next_shark_axis[r][c].append([r, c, s, 0, z])
                else:
                    divide = abs(diff) // max_row_move
                    rest = abs(diff) % max_row_move

                    if divide%2 == 0:
                        r = 1 + rest
                        key = str(r) +" "+ str(c)
                        next_shark_axis[r][c].append([r, c, s, 1, z])
                        next_axis_dic[key] = 1
                    else:
                        r = R - rest
                        next_shark_axis[r][c].append([r, c, s, 0, z])
                        key = str(r) +" "+ str(c)
                        next_axis_dic[key] = 1
            elif d == 1:
                diff = (R-r) - s

                if diff >= 0:
                    r += s
                    key = str(r) +" "+ str(c)
                    next_axis_dic[key] = 1
                    next_shark_axis[r][c].append([r, c, s, 1, z])
                else:
                    divide = abs(diff) // max_row_move
                    rest = abs(diff) % max_row_move

                    if divide%2 == 0:
                        r = R - rest
                        next_shark_axis[r][c].append([r, c, s, 0, z])
                        key = str(r) +" "+ str(c)
                        next_axis_dic[key] = 1
                    else:
                        r = 1 + rest
                        next_shark_axis[r][c].append([r, c, s, 1, z])
                        key = str(r) +" "+ str(c)
                        next_axis_dic[key] = 1
            elif d == 2:
                diff = (C - c) - s

                if diff >= 0:
                    c += s
                    key = str(r) +" "+ str(c)
                    next_axis_dic[key] = 1
                    next_shark_axis[r][c].append([r, c, s, 2, z])
                else:
                    divide = abs(diff) // max_col_move
                    rest = abs(diff) % max_col_move

                    if divide%2==0:
                        c = C - rest
                        next_shark_axis[r][c].append([r, c, s, 3, z])
                        key = str(r) +" "+ str(c)
                        next_axis_dic[key] = 1
                    else:
                        c = 1 + rest
                        next_shark_axis[r][c].append([r, c, s, 2, z])
                        key = str(r) +" "+ str(c)
                        next_axis_dic[key] = 1
            else:
                diff = (c - 1) - s

                if diff >= 0:
                    c -= s
                    key = str(r) +" "+ str(c)
                    next_axis_dic[key] = 1
                    next_shark_axis[r][c].append([r, c, s, 3, z])
                else:
                    divide = abs(diff)// max_col_move
                    rest = abs(diff) % max_col_move

                    if divide%2 == 0:
                        c = 1 + rest
                        next_shark_axis[r][c].append([r, c, s, 2, z])
                        key = str(r) +" "+ str(c)
                        next_axis_dic[key] = 1
                    else:
                        c = C - rest
                        next_shark_axis[r][c].append([r, c, s, 3, z])
                        key = str(r) +" "+ str(c)
                        next_axis_dic[key] = 1

    for key in next_axis_dic.keys():
        i, j = key.split(' ')
        i, j = int(i), int(j)
        next_shark_axis[i][j].sort(key=lambda x:-x[4])
        next_shark_axis[i][j] = [next_shark_axis[i][j][0]]

    axis_dic = next_axis_dic
    shark_axis = next_shark_axis

print(ans)
