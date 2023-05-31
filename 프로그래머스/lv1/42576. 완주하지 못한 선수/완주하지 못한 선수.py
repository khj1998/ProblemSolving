def solution(participant, completion):
    answer = ''
    dic = {}
    
    for p in participant:
        if p not in dic.keys():
            dic[p] = 1
        else:
            dic[p] += 1
    
    for comp in completion:
        dic[comp]-=1
    
    for key in dic.keys():
        if dic[key]!=0:
            answer=key
            break
    
    return answer