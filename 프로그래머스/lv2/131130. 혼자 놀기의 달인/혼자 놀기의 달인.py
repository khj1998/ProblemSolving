def solution(cards):
    answer = 0
    
    for i in range(len(cards)):
        cards[i] = cards[i]-1
    
    for box_num in range(len(cards)):
        check = [False]*100
        first = []
        first.append(box_num)
        check[box_num] = True
        box_num = cards[box_num]
        
        while not check[box_num]:
            first.append(box_num)
            check[box_num] = True
            box_num = cards[box_num]       
        
        next_boxes = []
        for i in cards:
            if not check[i]:
                next_boxes.append(i)
        
        for box_num in next_boxes:
            second = []
            second.append(box_num)
            check[box_num] = True
            box_num = cards[box_num]
            
            while not check[box_num]:
                second.append(box_num)
                check[box_num] = True
                box_num = cards[box_num]
            
            for i in next_boxes:
                check[i] = False
            
            if len(next_boxes)==0:
                continue
            else:
                answer=max(answer,len(first)*len(second))
            
    
    return answer