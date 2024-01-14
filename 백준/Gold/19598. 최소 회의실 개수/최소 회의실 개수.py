import sys
input = sys.stdin.readline
import heapq

N = int(input())
ans = 0
array = []
end_time = []

for _ in range(N):
    start,end = map(int,input().split())
    array.append((start,end))

array.sort(key = lambda x:(-x[0],-x[1]))

while array:
    start,end = array.pop()

    if not end_time:
        ans+=1
        heapq.heappush(end_time,end)
        continue

    if end_time[0] > start:
        heapq.heappush(end_time,end)
        ans+=1
    else:
        heapq.heappop(end_time)
        heapq.heappush(end_time,end)

print(ans)
