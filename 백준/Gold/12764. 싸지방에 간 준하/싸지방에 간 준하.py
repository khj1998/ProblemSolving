import sys
input = sys.stdin.readline
import heapq

N = int(input())
times = []
count = []
computer = []
time_min_heap = []
com_count = [0] * (N+1)
max_ans = 0

for i in range(1,N+1):
    a,b = map(int,input().split())
    times.append((a,b))
    heapq.heappush(count,i)

times.sort()

for time in times:
    start,end = time

    while time_min_heap and start > time_min_heap[0][0]:
        end_time,c = heapq.heappop(time_min_heap)
        heapq.heappush(count,c)

    c = heapq.heappop(count)
    com_count[c] += 1
    heapq.heappush(time_min_heap,[end,c])
    max_ans = max(max_ans,len(time_min_heap))

print(max_ans)

for i in range(1,max_ans+1):
    print(com_count[i],end = " ")
