def solution(n, times):
    answer = 1000000001
    start,end = 1,int(1e14)
    
    while start<=end:
        mid = (start+end)//2
        count = 0
        
        for time in times:
            count += (mid//time)
        
        if count >= n:
            answer = mid
            end = mid -1
        else:
            start = mid + 1
            
    return answer