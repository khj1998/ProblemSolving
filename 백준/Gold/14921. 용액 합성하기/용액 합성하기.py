import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int,input().split()))
array.sort()
start,end = 0,N-1
ans = int(1e9)

while start<end:
    result = array[start]+array[end]

    if result >= 0:
        end -= 1
        if abs(result) < abs(ans):
            ans = result
    else:
        start += 1
        if abs(result) < abs(ans):
            ans = result

print(ans)
