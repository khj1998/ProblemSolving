def solution(lottos, win_nums):
    answer = []
    low,high = 0,0
    zero_cnt = 0
    
    for lotto in lottos:
        if lotto == 0:
            zero_cnt+=1
            continue
        for num in win_nums:
            if lotto==num:
                low+=1
    
    high = low+zero_cnt
    
    if low < 2:
        low = 6
    else:
        low = 7-low
    
    if high == 0:
        answer = [6,6]
    else:
        answer=[7-high,low]
    
    return answer