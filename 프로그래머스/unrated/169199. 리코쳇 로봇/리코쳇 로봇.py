from collections import deque

dx,dy = [-1,1,0,0],[0,0,-1,1]

def solution(board):  
    answer = 0
    q = deque()
    row,col = len(board),len(board[0])
    
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                start_x,start_y = i,j
                q.append((start_x,start_y,0))
    
    check = [[int(1e8)]*col for _ in range(row)]
    
    while q:
        x,y,cnt = q.popleft()
        
        if board[x][y] == 'G':
            return cnt
        
        for i in range(4):
            next_x,next_y = x,y
            
            while 0<=next_x + dx[i]<row and 0<=next_y + dy[i]<col and board[next_x + dx[i]][next_y + dy[i]]!='D':
                next_x += dx[i]
                next_y += dy[i]
            
            if check[next_x][next_y] > cnt+1:
                check[next_x][next_y] = cnt+1
                q.append((next_x,next_y,cnt+1))
            
    return -1