import heapq

def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    
    answer = 0
    q = []
    
    for num in enemy:
        army_cnt =  n-num
        
        if army_cnt < 0:
            if k == 0:
                break
            defence_cnt = heapq.heappushpop(q,-num)
            n  = army_cnt - defence_cnt
            k -= 1
            answer+=1
        else:
            n = army_cnt
            heapq.heappush(q,-num)
            answer += 1
    
    return answer