import heapq

def solution(n, k, enemy):
    answer = 0
    q = []
    
    for e_num in enemy:
        n -= e_num
        
        if n<0:
            if k == 0:
                break
            else:
                num = heapq.heappushpop(q,-e_num)
                n -= num
                k-=1
                answer+=1
        else:
            heapq.heappush(q,-e_num)    
            answer+=1
    
    return answer