def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize==0:
        return 5*len(cities)
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            answer+=1
            
            for i in range(len(cache)):
                if cache[i] == city:
                    cache.pop(i)
                    cache.append(city)
                    break
        else:
            answer+=5
            
            if len(cache) == cacheSize:
                cache.pop(0)
                cache.append(city)
            else:
                cache.append(city)
                
    return answer