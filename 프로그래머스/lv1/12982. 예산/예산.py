def solution(d, budget):
    answer = 0
    total_need = 0
    d.sort()
    
    for req in d:
        total_need+=req
        if total_need <= budget:
            answer+=1
        else:
            break
    return answer