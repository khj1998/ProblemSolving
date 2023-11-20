from collections import defaultdict
from bisect import bisect_left
from itertools import combinations

def solution(info, query):
    answer = []
    dic = defaultdict(list)
    
    #각 정보마다 모든 경우의 수를 구한다.
    for i in info:
        temp = i.split()
        temp[-1] = int(temp[-1])
        
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    for d in range(2):
                        key = ''
                        if a == 0:
                            key += temp[0]
                        else:
                            key += '-'
                        if b == 0:
                            key += temp[1]
                        else:
                            key += '-'
                        if c == 0:
                            key += temp[2]
                        else:
                            key += '-'
                        if d == 0:
                            key += temp[3]
                        else:
                            key += '-'
 
                        if key not in dic.keys():
                            dic[key] = [temp[-1]]
                        else:
                            dic[key].append(temp[-1])
    
    for key in dic.keys():
        dic[key].sort()
    
    for q in query:
        q = q.split(' and ')
        temp = q[-1].split()
        q[-1] = temp[0]
        score = int(temp[-1])
        q = ''.join(q)
        
        if q in dic.keys():
            idx = bisect_left(dic[q],score)
            answer.append(len(dic[q])-idx)
        else:
            answer.append(0)
    
    return answer