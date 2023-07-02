def solution(ingredient):
    answer = 0
    idx = 0
    l = len(ingredient)
    ans = '1231'
    s = ''
    temp = []
    
    for i in ingredient:
        s+=str(i)
    
    while idx < l:
        temp.append(s[idx])
        
        if ''.join(temp[-4:]) == ans:
            answer+=1
            
            for _ in range(4):
                temp.pop()
        
        idx+=1
    
    return answer