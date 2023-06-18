def solution(dirs):
    answer = 0
    path = []
    x,y = 0,0
    temp = [1,2,3,4]
    
    for d in dirs:
        start_x,start_y = x,y
        if d=="U":
            y = y+1
        elif d=="D":
            y = y-1
        elif d=="R":
            x = x+1
        else:
            x = x-1
        
        if (x>=-5 and x<=5) and (y>=-5 and y<=5):
            if ([start_x,start_y,x,y] not in path) and ([x,y,start_x,start_y] not in path):
                path.append([start_x,start_y,x,y])
                answer+=1
        else:
            x,y = start_x,start_y
        
    return answer