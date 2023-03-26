def solution(k, tangerine):
    dic = {}
    for data in tangerine:
        if data not in dic.keys():
            dic[data] = 1
        else:
            dic[data] += 1
    dic = sorted(dic.items(),key = lambda x:x[1])
    total_num = len(tangerine)
    types = len(dic)
    
    for i in range(types):
        key,value = dic[i]
        total_num -= value
        
        if total_num == k:
            types -= (i+1)
            break
        elif total_num < k:
            types -= i
            break
            
    return types