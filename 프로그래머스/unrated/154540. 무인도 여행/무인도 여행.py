from collections import deque

def find_foods(x,y,maps,check):
    dx,dy = [0,0,-1,1],[-1,1,0,0]
    q = deque()
    q.append((x,y))
    ans = int(maps[x][y])
    check[x][y] = True
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            px = x+dx[i]
            py = y+dy[i]
            
            if 0<=px<row and 0<=py<col:
                if maps[px][py] == 'X' or check[px][py]:
                    continue
                ans+=int(maps[px][py])
                check[px][py] = True
                q.append((px,py))
    return ans

def solution(maps):
    global row,col
    
    answer = []
    row,col = len(maps),len(maps[0])
    check = [[False]*col for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            if maps[i][j] != 'X' and not check[i][j]:
                answer.append(find_foods(i,j,maps,check))
    
    if not answer:
        answer = [-1]
    else:
        answer.sort()
        
    return answer