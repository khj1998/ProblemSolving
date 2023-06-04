from copy import deepcopy

def solution(skill, skill_trees):
    answer = 0
    arr = []
    dic = {}
    
    for i in range(len(skill)):
        dic[skill[i]] = i
        arr.append(i)
    
    for tree in skill_trees:
        isPossible = True
        tmp_arr = deepcopy(arr)
        
        for t in tree:
            if t not in skill:
                continue
            else:
                idx = dic[t]
                if tmp_arr[idx] == 0:
                    for i in range(idx+1,len(tmp_arr)):
                        tmp_arr[i]-=1
                else:
                    isPossible = False
                    break
                    
        if isPossible:
            answer+=1
    
    return answer