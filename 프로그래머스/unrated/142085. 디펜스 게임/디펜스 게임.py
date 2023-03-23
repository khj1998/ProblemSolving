import heapq

def solution(n, k, enemy):
    answer = 0
    q = []
    total_enemy = 0
    
    for e in enemy:
        total_enemy += e
        
        if total_enemy <= n:
            heapq.heappush(q,-e)
            answer+=1
        elif k > 0:
            total_enemy += heapq.heappushpop(q,-e)
            k-=1
            answer+=1
        
    return answer