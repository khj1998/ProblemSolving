from itertools import combinations
from bisect import bisect_left

def solution(dice):
    answer = []
    n = len(dice)
    idx_list = [i for i in range(n)]
    a_dice_list = list(combinations(idx_list,n//2))
    max_win_cnt = 0
    
    def dfs(dice_list,depth,result,sum_list):
        if depth == n//2:
            sum_list.append(result)
            return
        
        for num in dice[dice_list[depth]]:
            dfs(dice_list,depth+1,result+num,sum_list)
    
    for a_list in a_dice_list:
        a_sums,b_sums = [],[]
        b_list = [i for i in range(n) if i not in a_list]
        
        dfs(a_list,0,0,a_sums)
        dfs(b_list,0,0,b_sums)
        
        b_sums.sort()
        win_cnt = 0
        
        for a_sum in a_sums:
            win_cnt += bisect_left(b_sums,a_sum)
        
        if win_cnt > max_win_cnt:
            max_win_cnt = win_cnt
            answer = [i+1 for i in a_list]
    
    return answer