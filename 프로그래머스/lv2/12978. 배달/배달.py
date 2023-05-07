from collections import deque

def set_distance(start,N,K):
    q = deque()
    INF = int(1e9)
    check = [False]*(N+1)
    distance = [INF]*(N+1)
    distance[1] = 0
    q.append((start,0))
    
    while q:
        now,dist = q.popleft()
        for b,cost in towns[now]:
            next_cost = dist+cost
            if next_cost <= distance[b]:
                if next_cost <= K:
                    distance[b] = next_cost
                    q.append((b,next_cost))
    return distance

def solution(N, road, K):
    global towns
    answer = 0
    towns = [[] for _ in range(N+1)]
    
    for a,b,c in road:
        towns[a].append((b,c))
        towns[b].append((a,c))
    
    distance = set_distance(1,N,K)
    for i in range(1,N+1):
        if distance[i] <= K:
            answer+=1
    
    return answer