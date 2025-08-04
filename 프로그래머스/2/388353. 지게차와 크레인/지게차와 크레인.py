from collections import deque

def solution(storage, requests):
    row,col = len(storage)+2, len(storage[0])+2
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    
    new_storage = [['0' for _ in range(col)] for _ in range(row)]
    
    for i in range(1,row-1):
        for j in range(1,col-1):
            new_storage[i][j] = storage[i-1][j-1]
    
    def find_reachable_target_area(target_char):
        q = deque()
        check = [[False for _ in range(col+2)] for _ in range(row+2)]
        
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row-1:
                    q.append((i,j))
                else:
                    q.append((i,0))
                    q.append((i,col-1))
        
        while q:
            x,y = q.popleft()
            
            for i in range(4):
                px = x + dx[i]
                py = y + dy[i]
                
                if 0 <= px <= row-1 and 0 <= py <= col-1 and check[px][py] == False:
                    if new_storage[px][py] == target_char:
                        new_storage[px][py] = '0'
                        check[px][py] = True
                    elif new_storage[px][py] == '0':
                        check[px][py] = True
                        q.append((px,py))
        
    
    def find_all_target_area(target_char):
        for i in range(row):
            for j in range(col):
                if new_storage[i][j] == target_char:
                    new_storage[i][j] = '0'
    
    def get_container_count():
        answer = 0
        
        for i in range(row):
            for j in range(col):
                if new_storage[i][j] != '0':
                    answer += 1
        
        return answer
    
    for request in requests:
        if len(request) == 1:
            find_reachable_target_area(request[0])
        else:
            find_all_target_area(request[0])
        
    return get_container_count()