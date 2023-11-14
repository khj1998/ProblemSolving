from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    dic = defaultdict(list)
    
    for r in records:
        r = r.split(' ')
        time = int(r[0][0:2]) * 60 + int(r[0][3:])
        
        if r[1] not in dic.keys():
            dic[r[1]] = [time]
        else:
            dic[r[1]].append(time)
    
    for key in dic.keys():
        max_time = 23*60 + 59
        start_time = 0
        total_time = 0
        for i in range(len(dic[key])):
            if i%2==0:
                start_time = dic[key][i]
            else:
                total_time += dic[key][i] - start_time
        
        if len(dic[key])%2 == 1:
            total_time += (max_time - dic[key][-1])
        
        total_fees = 0
        
        if total_time <= fees[0]:
            total_fees = fees[1]
        else:
            total_fees = fees[1] + math.ceil((total_time-fees[0])/fees[2])*fees[3]
        
        answer.append((int(key),total_fees))
    
    answer.sort()
    ans = [j for i,j in answer]
    
    return ans