def solution(want, number, discount):
    answer = 0
    dic = {}
    ans_num = {}
    
    for i in range(len(want)):
        ans_num[want[i]] = number[i]
        dic[want[i]] = 0
    
    for i in range(10):
        if discount[i] not in dic.keys():
            dic[discount[i]] = 0
        else:
            dic[discount[i]] += 1
    
    start = 0
    end = 9
    total = len(discount) -1
    
    while True:
        isJoin = True
        
        for i in dic.keys():
            if i not in ans_num.keys():
                continue
            if dic[i] < ans_num[i]:
                isJoin = False
                break
        
        if isJoin:
            answer+=1
        
        dic[discount[start]] -= 1
        start+=1
        end+=1
        
        if end>total:
            break
        
        if discount[end] not in dic.keys():
            dic[discount[end]] = 1
        else:
            dic[discount[end]] += 1
    
    return answer