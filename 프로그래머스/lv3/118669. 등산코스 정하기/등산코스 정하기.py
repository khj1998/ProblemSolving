import heapq
    
def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n+1)]    
    summits_set = set(summits)
    
    for x,y,length in paths:
        graph[x].append([y,length])
        graph[y].append([x,length])
    
    def dijkstra():
        q=[]
        INF = int(1e9)
        distance = [INF] * (n+1)
        result = []
        
        for gate in gates:
            distance[gate] = 0
            heapq.heappush(q,(0,gate))
        
        while q:
            now_intense,now = heapq.heappop(q)
            
            if distance[now] < now_intense:
                continue
            
            if now in summits_set:
                result.append((now,now_intense))
                continue
            
            for Next,cost in graph[now]:
                temp_intense = max(now_intense,cost)
                
                if distance[Next] > temp_intense:
                    distance[Next] = temp_intense
                    heapq.heappush(q,(temp_intense,Next))
        
        return result
    
    answer = dijkstra()
    answer.sort(key = lambda x:(x[1],x[0]))
    return answer[0]