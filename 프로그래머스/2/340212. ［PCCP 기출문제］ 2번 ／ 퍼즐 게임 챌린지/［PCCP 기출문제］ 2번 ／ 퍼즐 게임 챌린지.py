# diff > level 소요시간 : time_cur + (diff-level) * (time_cur + time_prev)
# diff <= level 소요시간 : time_cur
def solution(diffs, times, limit):
    answer = 0
    start,end = 1,100000
    
    while start<=end:
        mid = (start+end)//2
        total_time = 0
        
        for i in range(len(diffs)):
            total_time+=times[i]
            
            if diffs[i] > mid:
                total_time += (diffs[i] - mid) * (times[i] + times[i-1])
        
        if total_time > limit:
            start = mid+1
        else:
            answer = mid
            end = mid-1
          
    return answer