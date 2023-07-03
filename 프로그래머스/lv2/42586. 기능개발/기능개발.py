import math

def solution(progresses, speeds):
    answer = []
    deploy = []
    
    if len(progresses)==1:
        return [1]
    
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        remain = math.ceil(remain/speeds[i])
        deploy.append(remain)
    
    num = 1
    last_day = deploy.pop(0)
        
    while deploy:
        day = deploy.pop(0)
        
        if day<=last_day:
            num+=1
        else:
            last_day = day
            answer.append(num)
            num = 1
    
    answer.append(num)
    
    return answer