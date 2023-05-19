def solution(k, score):
    answer = []
    temp = []
    
    for s in score:
        if len(temp) < k:
            temp.append(s)
            temp.sort()
        elif temp[0] < s:
            temp.pop(0)
            temp.append(s)
            temp.sort()
        answer.append(temp[0])
        
    return answer