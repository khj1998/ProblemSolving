from collections import deque

def solution(queue1, queue2):
    answer = 0
    max_cnt = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    while queue1 and queue2:
        if sum1==sum2:
            return answer
        
        if answer>=600000:
            break
        
        if sum1>sum2:
            p1 = queue1.popleft()
            sum1-=p1
            queue2.append(p1)
            sum2+=p1
        elif sum1<sum2:
            p2 = queue2.popleft()
            sum2-=p2
            queue1.append(p2)
            sum1+=p2
        
        answer+=1
        
    return -1