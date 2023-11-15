def solution(s):
    answer = []
    
    s = s[2:-2].split('},{')
    new_s,dic = [],{}
    
    for s_list in s:
        s_list = s_list.split(',')
        new_s.append(s_list)
        
    new_s.sort(key = len)
    
    for l in new_s:
        for num in l:
            if num not in dic.keys():
                dic[num] = 1
                answer.append(int(num))
        
    return answer