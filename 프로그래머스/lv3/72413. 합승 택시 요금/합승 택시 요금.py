import heapq

def solo(n,edges,start,end):
    q = []
    INF = int(1e8)
    distance = [INF]*(n+1)
    distance[start] = 0
    heapq.heappush(q,(start,0))
    
    while q:
        now,dist = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        
        for Next,cost in edges[now]:
            next_cost = dist+cost
            if next_cost < distance[Next]:
                distance[Next] = next_cost
                heapq.heappush(q,(Next,next_cost))
    
    return distance[end]

def get_together_stop(n,edges,start):
    q = []
    INF = int(1e8)
    distance = [INF]*(n+1)
    distance[start] = 0
    heapq.heappush(q,(start,0))
    
    while q:
        now,dist = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        
        for Next,cost in edges[now]:
            next_cost = dist+cost
            
            if next_cost < distance[Next]:
                distance[Next] = next_cost
                heapq.heappush(q,(Next,next_cost))
    
    return distance

def get_each_cost(n,edges,distance,start,end):
    q = []
    INF = int(1e8)
    ans_cost = [INF]*(n+1)
    ans_cost[start] = 0
    heapq.heappush(q,(start,0))
    
    while q:
        now,dist = heapq.heappop(q)
        
        if ans_cost[now] < dist:
            continue
        
        for Next,cost in edges[now]:
            next_cost = dist + cost
            
            if next_cost < ans_cost[Next]:
                ans_cost[Next] = next_cost
                heapq.heappush(q,(Next,next_cost))
                
    return ans_cost[end]

def solution(n, s, a, b, fares):
    answer = 0
    INF = int(1e8)
    edges = [[] for _ in range(n+1)]
    
    for x,y,cost in fares:
        edges[x].append((y,cost))
        edges[y].append((x,cost))
    
    a_solo = solo(n,edges,s,a)
    b_solo = solo(n,edges,s,b)
    
    distance = get_together_stop(n,edges,s)
    total_cost = INF
    
    for i in range(1,n+1):
        if distance[i]!=INF:
            a_cost = get_each_cost(n,edges,distance,i,a)
            b_cost = get_each_cost(n,edges,distance,i,b)
            total_cost = min(total_cost,distance[i]+a_cost+b_cost)
    
    answer = min(a_solo+b_solo,total_cost)
    
    return answer