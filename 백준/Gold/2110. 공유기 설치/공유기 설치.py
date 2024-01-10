import sys
input = sys.stdin.readline

N,C = map(int,input().split())
ans = 0
array = []

for _ in range(N):
    array.append(int(input()))

array.sort()
left,right = 0,array[-1] - array[0]

while left<=right:
    mid = (left+right)//2
    cnt = 1
    dist = 0

    for i in range(1,N):
        dist += (array[i] - array[i-1])

        if dist >= mid:
            cnt+=1
            dist = 0

    if cnt < C:
        right = mid-1
    else:
        ans = mid
        left = mid + 1

print(ans)
