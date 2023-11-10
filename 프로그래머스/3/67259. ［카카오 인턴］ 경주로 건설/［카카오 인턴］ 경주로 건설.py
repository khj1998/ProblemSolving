from collections import deque

def solution(board):
    N = len(board)
    q = deque()
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    INF = int(1e8)
    array = [[[INF]* 4 for _ in range(N)] for _ in range(N)]
    
    for k in range(4):
        array[0][0][k] = 0
        q.append((0,0,0,k))
    
    while q:
        x,y,now_cost,direc = q.popleft()
        
        for i in range(4):
            px = x+dx[i]
            py = y+dy[i]
            
            if 0<=px<N and 0<=py<N and board[px][py] == 0:
                # 코너
                if (i in (0,1) and direc in (2,3)) or (i in (2,3) and direc in (0,1)):
                    if array[px][py][i] > now_cost + 600:
                        array[px][py][i] = now_cost + 600
                        q.append((px,py,array[px][py][i],i))
                else: # 직선도로
                    if array[px][py][direc] > now_cost + 100:
                        array[px][py][direc] = now_cost + 100
                        q.append((px,py,array[px][py][direc],direc))

    return min(array[N-1][N-1])