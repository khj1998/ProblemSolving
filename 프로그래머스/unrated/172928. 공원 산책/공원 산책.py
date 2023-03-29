def solution(park, routes):
    answer = []
    row = len(park)
    col = len(park[0])
    now_x,now_y = -1,-1
    
    for i in range(row):
        for j in range(col):
            if park[i][j] == "S":
                now_x,now_y = i,j
        if now_x!=-1:
            break
    
    for s in routes:
        direc = s[0]
        cnt = int(s[2])
        save_x,save_y = now_x,now_y
        
        if direc == "N":
            while cnt > 0:
                now_x -= 1
                cnt -= 1
                if now_x < 0 or park[now_x][now_y] == "X":
                    now_x,now_y = save_x,save_y
                    break                    
        if direc == "S":
            while cnt > 0:
                now_x += 1
                cnt -= 1
                if now_x >= row or park[now_x][now_y] == "X":
                    now_x,now_y = save_x,save_y
                    break                  
        if direc == "W":
            while cnt > 0:
                now_y -= 1
                cnt -= 1
                if now_y < 0 or park[now_x][now_y] == "X":
                    now_x,now_y = save_x,save_y
                    break                  
        if direc == "E":
            while cnt > 0:
                now_y += 1
                cnt -= 1
                if now_y >= col or park[now_x][now_y] == "X":
                    now_x,now_y = save_x,save_y
                    break                 
    
    answer = [now_x,now_y]
    return answer