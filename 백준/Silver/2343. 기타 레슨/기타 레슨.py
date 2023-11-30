import sys
input = sys.stdin.readline

N,M = map(int,input().split())
answer = []
times = list(map(int,input().split()))
start = max(times)
end = sum(times)

while start <= end:
    mid = (start+end)//2
    total_time_cnt = 0
    cnt = 0
    temp_size = 0

    for time in times:
        total_time_cnt += time

        if total_time_cnt >= mid:
            cnt += 1

            if total_time_cnt == mid:
                temp_size = max(temp_size, total_time_cnt)
                total_time_cnt = 0
            else:
                temp_size = max(temp_size, total_time_cnt - time)
                total_time_cnt = time

    if total_time_cnt > 0:
        cnt += 1
        temp_size = max(temp_size,total_time_cnt)

    if cnt > M:
        start = mid+1
    elif cnt <= M:
        end = mid-1
        answer.append(temp_size)

print(min(answer))