import sys
import heapq
input=sys.stdin.readline

N=int(input())
array=[]
q=[]
for _ in range(N):
    a=int(input())
    if a==0:
        if len(q)==0:
            array.append(0)
        else:
            array.append(heapq.heappop(q))
    else:
        heapq.heappush(q,a)

for i in range(len(array)):
    print(array[i])