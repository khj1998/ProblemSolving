from collections import deque

def solution(cacheSize, cities):
    answer = 0
    stack = []
    
    for city in cities:
        city = city.lower()
        
        if city in stack:
            answer+=1
            stack.pop(stack.index(city))
            stack.append(city)
            continue
        else:
            answer +=5
        
        if cacheSize>0 and len(stack) == cacheSize:
            stack.pop(0)
            stack.append(city)
        elif len(stack) < cacheSize:
            stack.append(city)
                
    return answer