def solution(n, times):
    answer = 0
    min_time,max_time = 1,max(times)*n
    
    while min_time <= max_time:
        count = 0
        mid = (min_time+max_time)//2
        
        for time in times:
            count += mid//time
        
        if count >= n:
            answer = mid
            max_time = mid-1
        else:
            min_time = mid+1
            
    return answer