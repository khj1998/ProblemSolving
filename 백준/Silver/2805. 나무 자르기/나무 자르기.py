import sys
input = sys.stdin.readline

N,M = map(int,input().split())
ans = 0
woods = list(map(int,input().split()))

left,right = 0,int(1e10)

# 절단기에 설정 가능한 높이의 최댓값 구하기
while left <= right:
    mid = (left+right)//2
    total_length = 0

    for wood in woods:
        diff = wood - mid

        if diff > 0:
            total_length+= diff

    if total_length >= M:
        ans = mid

        if total_length == M:
            break
        left = mid + 1
    else:
        right = mid -1

print(ans)