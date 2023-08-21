def solution(routes):
    answer = 1
    routes.sort(key = lambda x:(x[1]))
    end = routes[0][1]
    
    for i in range(1,len(routes)):
        if routes[i][0] > end:
            answer+=1
            end = routes[i][1]
    
    return answer