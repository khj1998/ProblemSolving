from collections import deque

def solution(maps):
    INF = int(1e8)
    answer = 0
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    
    start_pos = []
    rever_pos = []
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start_pos = [i,j]
            if maps[i][j] == 'L':
                rever_pos = [i,j]
    
    def get_min_distance(destination_char,start):
        q = deque()
        q.append(start)
        map_distance = [[INF for _ in range(len(maps[0]))] for _ in range(len(maps))]
        map_distance[start[0]][start[1]] = 0
        
        while q:
            x,y = q.popleft()
            
            if maps[x][y] == destination_char:
                break
            
            for i in range(4):
                px = x+dx[i]
                py = y+dy[i]
                
                if 0<=px<len(maps) and 0<= py < len(maps[0]) and map_distance[px][py] > map_distance[x][y] + 1 and maps[px][py] != 'X':
                    map_distance[px][py] = map_distance[x][y] + 1
                    q.append([px,py])
        print(map_distance)
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] == destination_char:
                    return map_distance[i][j]
    
    answer += get_min_distance('L',start_pos)
    answer += get_min_distance('E',rever_pos)
    
    if answer >= INF:
        return -1
    return answer
