def solution(elements):
    max_cnt = len(elements)
    elements = elements*2
    result = set()
    
    for i in range(1,max_cnt+1):
        for j in range(max_cnt):
            result.add(sum(elements[j:j+i]))
            
    return len(result)