import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dx,dy = [-1,0,1,0],[0,1,0,-1]
space = []
ans = 0
x,y,d = map(int,input().split())

for _ in range(N):
    space.append(list(map(int,input().split())))

# 0: 북쪽 1: 동쪽 2: 남쪽 3: 서쪽
while True:
    if space[x][y] == 0 or space[x][y] == 2:
        if space[x][y] == 0:
            ans += 1
            space[x][y] = 2
        is_empty = False

        for i in range(4):
            px,py = x+dx[i],y+dy[i]

            if 0<=px<N and 0<=py<M and space[px][py]==0:
                is_empty = True
                break
        
        if not is_empty:
            back_direc = (d+2)%4
            px,py = x+dx[back_direc],y+dy[back_direc]

            if 0<=px<N and 0<=py<M:
                if space[px][py]==1:
                    break

                x,y=px,py
        else:
            d = (d+3) % 4
            px,py = x+dx[d] , y+dy[d]

            if 0<=px<N and 0<=py<M and space[px][py] == 0:
                x,y = px,py

print(ans)
