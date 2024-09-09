from collections import deque

def solution(maps):
    answer = []
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    row,col = len(maps),len(maps[0])
    check = [[False]*col for _ in range(row)]
    
    def get_area(x,y):
        area = 0
        q =deque()
        check[x][y] = True
        q.append((x,y))
        
        while q:
            x,y = q.popleft()
            area += int(maps[x][y])
            
            for i in range(4):
                px,py = x+dx[i],y+dy[i]
                
                if 0<=px<row and 0<=py<col and not check[px][py] and maps[px][py]!='X':
                    check[px][py] = True
                    q.append((px,py))
        return area
    
    for i in range(row):
        for j in range(col):
            if maps[i][j] != 'X' and not check[i][j]:
                answer.append(get_area(i,j))
    
    if not answer:
        return [-1]
    else:
        answer.sort()
        return answer