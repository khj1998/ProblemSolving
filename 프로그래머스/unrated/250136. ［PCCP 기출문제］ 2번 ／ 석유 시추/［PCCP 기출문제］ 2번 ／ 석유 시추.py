from collections import defaultdict,deque

def solution(land):
    answer = 0
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    row,col = len(land),len(land[0])
    oil_cols = [0 for _ in range(col)]
    check = [[False]*col for _ in range(row)]
    
    def bfs(x,y):
        cnt = 1
        q = deque()
        q.append((x,y))
        min_y,max_y = 501,-1
        check[x][y] = True
        
        while q:
            x,y = q.popleft()
            min_y,max_y = min(min_y,y),max(max_y,y)
            
            for i in range(4):
                px,py = x+dx[i],y+dy[i]
                
                if 0<=px<row and 0<=py<col and land[px][py] == 1 and not check[px][py]:
                    cnt += 1
                    check[px][py] = True
                    q.append((px,py))
        
        for i in range(min_y,max_y+1):
            oil_cols[i]+=cnt
    
    for i in range(row):
        for j in range(col):
            if land[i][j] == 1 and not check[i][j]:
                bfs(i,j)
    
    for i in range(col):
        answer = max(answer,oil_cols[i])
    
    return answer