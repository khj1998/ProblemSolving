import sys
input=sys.stdin.readline

N=int(input())
array=[]
for _ in range(N):
    a,b=map(int,input().split())
    array.append((a,b))

array=sorted(array,key=lambda time:time[0])
array=sorted(array,key=lambda time:time[1])

count=0
start_time=0

for i in range(N):
    if start_time<=array[i][0]:
        count+=1
        start_time=array[i][1]

print(count)