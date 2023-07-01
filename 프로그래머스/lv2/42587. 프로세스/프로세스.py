from copy import deepcopy

def solution(priorities, location):
    answer = 1
    process = []
    
    for i in range(len(priorities)) :
        process.append((i,priorities[i]))
    
    while True:
        temp = deepcopy(process)
        temp.sort(key = lambda x:-x[1])
        
        idx,priority = process.pop(0)
        
        if priority == temp[0][1]:
            if idx==location:
                break
            else:
                answer+=1
        else:
            process.append((idx,priority))            
                        
    return answer