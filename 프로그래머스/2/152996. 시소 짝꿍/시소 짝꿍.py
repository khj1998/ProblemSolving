from collections import Counter

def solution(weights):
    answer = 0
    weights = Counter(weights)
    rate = [2/3,2/4,3/4]
    
    for key in weights.keys():
        if weights[key] > 1:
            n = weights[key]
            answer += (n*(n-1))//2
    
    weights_set = set(weights)
    
    for w in weights_set:
        if w*rate[0] in weights_set:
            answer += (weights[w*rate[0]] * weights[w])
        if w*rate[1] in weights_set:
            answer += (weights[w*rate[1]] * weights[w])
        if w*rate[2] in weights_set:
            answer += (weights[w*rate[2]] * weights[w])

    return answer