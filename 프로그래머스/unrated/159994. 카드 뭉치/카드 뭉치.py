def solution(cards1, cards2, goal):
    answer = ""
    cnt = 0
    
    for s in goal:
        if cards1 and s==cards1[0]:
            cnt+=1
            cards1.pop(0)
            continue
        if cards2 and s==cards2[0]:
            cnt+=1
            cards2.pop(0)
    
    if cnt == len(goal):
        answer = "Yes"
    else:
        answer="No"
    
    return answer