from collections import deque

def solution(maps):
    INF = int(1e8)
    answer = INF
    q = deque()
    row,col = len(maps),len(maps[0])
    L_x,L_y = -1,-1
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    check = [[INF]*col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if maps[i][j] == 'S':
                q.append((i,j,0))
                check[i][j] = 0
            if maps[i][j] == 'L':
                L_x,L_y = i,j
    
    while q:
        x,y,dist = q.popleft()
        
        if maps[x][y] == 'L':
            break;
        
        for i in range(4):
            px = x+dx[i]
            py = y+dy[i]
            
            if 0<=px<row and 0<=py<col:
                if maps[px][py]!='X' and check[px][py] > dist+1:
                    check[px][py] = dist+1
                    q.append((px,py,dist+1))
    
    if check[L_x][L_y] == INF:
        return -1
    else:
        q = deque()
        L_dist = check[L_x][L_y]
        q.append((L_x,L_y,0))
        check = [[INF]*col for _ in range(row)]
        check[L_x][L_y] = 0
        is_success = False
        
        while q:
            x,y,dist = q.popleft()
            
            if maps[x][y] == 'E':
                is_success = True
                answer = min(answer,L_dist+dist)
                break
            
            for i in range(4):
                px = x+dx[i]
                py = y+dy[i]
                
                if 0<=px<row and 0<=py<col:
                    if maps[px][py]!='X' and check[px][py] > dist+1:
                        check[px][py] = dist+1
                        q.append((px,py,dist+1))
        if not is_success:
            return -1
    
    return answer