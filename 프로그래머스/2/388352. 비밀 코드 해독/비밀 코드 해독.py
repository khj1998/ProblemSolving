from itertools import combinations

def solution(n, q, ans):
    answer = 0
    arr = list(combinations([i for i in range(1,n+1)],5))
    
    for arr_list in arr:
        secret_arr_index = 0
        temp = [0 for _ in range(len(q))]
        
        for i in range(len(q)):
            for data in q[i]:
                if data in arr_list:
                    temp[i] += 1
                    
        can_be_secret = True
        
        for i in range(len(temp)):
            if temp[i] != ans[i]:
                can_be_secret = False
            if not can_be_secret:
                break
        
        if can_be_secret:
            answer+=1
        
        secret_arr_index += 1
        
    return answer