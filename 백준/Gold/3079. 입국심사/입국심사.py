import sys
input = sys.stdin.readline

N,M = map(int,input().split())
ans = 0
judge = []

for _ in range(N):
    judge.append(int(input()))

left,right = min(judge),max(judge) * M

while left <= right:
    mid = (left + right) // 2
    total_cnt = 0

    for x  in judge:
        total_cnt += (mid//x)

    if total_cnt >= M: # 인원 수보다 많다. 값을 줄여야한다.
         ans = mid
         right = mid - 1
    elif total_cnt < M: # 인원 수보다 적다. 값을 늘려야 한다.
         left = mid + 1

print(ans)