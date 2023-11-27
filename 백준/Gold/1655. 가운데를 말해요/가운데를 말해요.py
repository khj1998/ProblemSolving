import sys
input=sys.stdin.readline
import heapq

n=int(input())
left=[]
right=[]
result=[]

for _ in range(n):
    num=int(input())

    if len(left)==len(right):
        heapq.heappush(left,(-num,num))
    else:
        heapq.heappush(right,(num,num))

    if right and right[0][0]<left[0][1]:
        min=heapq.heappop(right)[0]
        max=heapq.heappop(left)[1]
        heapq.heappush(left,(-min,min))
        heapq.heappush(right,(max,max))

    result.append(left[0][1])

for i in range(len(result)):
    print(result[i])