import sys
input = sys.stdin.readline

# 각 학생 배치때마다 다음 구현, 그리드 정렬 기준
# 각 그리드 마다 인접한 칸에 좋아하는 학생 수 많은 순
# 인접칸 중 비어있는 칸 많은 순
# 행의 번호가 작은 순
# 열의 번호가 작은 순
# (좋아하는 학생 수, 비어있는 칸 수, 행 번호, 열 번호)
# 자리 배치가 끝난 후 학생의 그리드 저장

N = int(input())
ans = 0
graph = [[-1]*N for _ in range(N)]
like_list =[[] for _ in range(N**2+1)]
dx,dy = [-1,1,0,0],[0,0,-1,1]

def get_grid_list(like_list):
    grid = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == -1:
                like_cnt,empty_cnt,row,col = 0,0,i,j

                for k in range(4):
                    px,py = i+dx[k],j+dy[k]

                    if 0<=px<N and 0<=py<N:
                        if graph[px][py] == -1:
                            empty_cnt+=1
                        elif graph[px][py] in like_list:
                            like_cnt+=1

                grid.append((like_cnt,empty_cnt,row,col))

    grid.sort(key = lambda x:(-x[0],-x[1],x[2],x[3]))
    return grid

def get_student_score(x,y,like_list):
    cnt = 0

    for i in range(4):
        px = x+dx[i]
        py = y+dy[i]

        if 0<=px<N and 0<=py<N:
            if graph[px][py] in like_list:
                cnt+=1

    if cnt == 0:
        return 0
    elif cnt == 1:
        return 1
    elif cnt == 2:
        return 10
    elif cnt == 3:
        return 100

    return 1000

for _ in range(N**2):
    array = list(map(int,input().split()))
    like_list[array[0]] = array[1:]
    grid = get_grid_list(array[1:])
    graph[grid[0][2]][grid[0][3]] = array[0]

for i in range(N):
    for j in range(N):
        ans += get_student_score(i,j,like_list[graph[i][j]])

print(ans)
