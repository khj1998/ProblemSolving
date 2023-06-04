def solution(food):
    answer = ''
    start = []
    end = []
    
    for i in range(1,len(food)):
        amount = food[i]
        
        if amount==1:
            continue
        start.append((i,amount//2))
        end.append((i,amount//2))
    end.reverse()
    
    while start or end:
        if start:
            num,count = start.pop(0)
            for i in range(count):
                answer+=str(num)
            if len(start)==0:
                answer+=str(0)
        else:
            num,count = end.pop(0)
            for i in range(count):
                answer+=str(num)
        
    return answer