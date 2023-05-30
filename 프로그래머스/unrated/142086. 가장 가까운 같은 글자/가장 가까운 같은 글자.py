def solution(s):
    answer = []
    pos = {}
    check = {}
    
    for i in range(len(s)):
        if s[i] not in pos.keys():
            check[s[i]] = False
    
    for i in range(len(s)):
        if not check[s[i]]:
            check[s[i]] = True
            answer.append(-1)
        else:
            answer.append(i-pos[s[i]])
        pos[s[i]] = i
            
    return answer