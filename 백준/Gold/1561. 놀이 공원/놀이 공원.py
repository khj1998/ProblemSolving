import sys
input = sys.stdin.readline

N,M = map(int,input().split())
array = list(map(int,input().split()))
time = 0
left,right = 0,max(array) * N

while left <= right:
    mid = (left+right)//2
    cnt = len(array)

    for i in array:
        cnt += mid//i

    if cnt >= N:
        time = mid
        right = mid-1
    else:
        left = mid+1

if N <= len(array):
    print(N)
else:
    total_num = len(array)

    for i in array:
        total_num += (time-1)//i

    for index,t in enumerate(array,start=1):
        if time%t == 0:
            total_num += 1

        if total_num == N:
            print(index)
            break
