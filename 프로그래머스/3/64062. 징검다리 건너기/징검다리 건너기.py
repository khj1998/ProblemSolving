def solution(stones, k):
    answer = 0
    left,right = 1,200000000
    
    while left <= right:
        cnt = 0
        mid = (left+right)//2
        
        for stone in stones:
            if mid >= stone:
                cnt+=1
            else:
                cnt=0
            
            if cnt >= k:
                break
        
        if cnt >= k:
            right = mid -1
        else:
            answer = mid
            left = mid + 1
        
    return answer+1