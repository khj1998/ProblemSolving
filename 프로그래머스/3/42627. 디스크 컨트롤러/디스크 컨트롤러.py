import heapq
import math

# 소요시간 짧은 순, 요청 시각 빠른 것, 작업 번호 작은 순 우선순위 높음
def solution(jobs):
    answer = 0
    total_job_count = len(jobs)
    current_time = 0
    job_index = 0
    q = []
    jobs.sort()
    
    while job_index < total_job_count or q:        
        while job_index < total_job_count and jobs[job_index][0] <= current_time:
            request_time, duration = jobs[job_index]
            heapq.heappush(q, (duration, request_time))
            job_index += 1
        
        if q:
            duration,request_time = heapq.heappop(q)
            current_time += duration
            answer += (current_time - request_time)
        else:
            current_time = jobs[job_index][0]

    return math.floor(answer/total_job_count)
