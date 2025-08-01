from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    
    for w in counter:
        if counter[w] > 1:
            answer += (counter[w] * (counter[w]-1))/2
    
    unique_weight = list(counter.keys())
    
    for w in unique_weight:
        #2,3
        if (w * 3)/2 in unique_weight:
            answer+= counter[w] * counter[(w*3)/2]
        #2,4
        if (w * 4)/2 in unique_weight:
            answer+= counter[w] * counter[(w*4)/2]
        
        #3,4
        if (w * 4)/3 in unique_weight:
            answer+= counter[w] * counter[(w*4)/3]
    
    return answer
