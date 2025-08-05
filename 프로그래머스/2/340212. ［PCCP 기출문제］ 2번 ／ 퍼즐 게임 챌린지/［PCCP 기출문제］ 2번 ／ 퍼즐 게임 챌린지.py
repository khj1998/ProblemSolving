def solution(diffs, times, limit):
    answer = 0
    start, end = 1, 100001 

    def calculate_total_time(now_diff,level,cur_times,prev_times):
        if now_diff <= level:
            return cur_times
        return (now_diff - level) * (cur_times + prev_times) + cur_times

    while start <= end:
        mid = (start + end) // 2
        total_times = 0
        
        for idx in range(len(times)):
            if idx == 0:
                total_times += calculate_total_time(diffs[idx],mid,times[idx],0)
            else:
                total_times += calculate_total_time(diffs[idx],mid,times[idx],times[idx-1])
        
        if total_times <= limit:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return answer