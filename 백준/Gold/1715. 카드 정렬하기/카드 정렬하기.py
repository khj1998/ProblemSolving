import sys
input = sys.stdin.readline
import heapq

N = int(input())
ans = 0
array = []

for _ in range(N):
    heapq.heappush(array,int(input()))

if N==1:
    print(0)
else:
    while array:
        x = heapq.heappop(array)
        y = 0

        if array:
            y = heapq.heappop(array)
        else:
            break

        ans += (x + y)
        heapq.heappush(array,x + y)

    print(ans)
