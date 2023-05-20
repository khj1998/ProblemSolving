def solution(keymap, targets):
    answer = []
    key_dic = {}
    
    for key in keymap:
        for idx,k in enumerate(key):
            if k not in key_dic.keys():
                key_dic[k] = idx+1
            else:
                key_dic[k] = min(idx+1,key_dic[k])
    
    for target in targets:
        cnt = 0
        canMade = True
        for c in target:
            if c in key_dic.keys():
                cnt += key_dic[c]
            else:
                canMade = False
                break
        if canMade:
            answer.append(cnt)
        else:
            answer.append(-1)
    
    return answer