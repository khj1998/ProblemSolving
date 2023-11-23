from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    dic = {}
    ans_dic = defaultdict(list)
    
    for order in orders:
        temp = [o for o in order]
        
        for num in course:
            combi = list(combinations(temp,num))
            
            if not combi:
                break
            
            for comb in combi:
                comb = list(comb)
                comb.sort()
                key = ''.join(comb)
                
                if key not in dic.keys():
                    dic[key] = 1
                else:
                    dic[key] += 1
    
    for key in dic.keys():
        if len(key) not in course:
            continue
        
        if len(key) not in ans_dic:
            ans_dic[len(key)] = [(dic[key],key)]
        else:
            ans_dic[len(key)].append((dic[key],key))
    
    for c in course:
        ans_dic[c].sort(reverse=True)
        max_val = -1
        
        for value,key in ans_dic[c]:
            if value > 1 and max_val <= value:
                max_val = value
                answer.append(key)
            else:
                break
    answer.sort()
    return answer