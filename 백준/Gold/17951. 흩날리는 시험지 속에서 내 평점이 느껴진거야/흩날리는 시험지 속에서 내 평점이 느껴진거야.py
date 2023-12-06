import sys
input = sys.stdin.readline

N,K = map(int,input().split())
test_list = list(map(int,input().split()))
start,end = min(test_list),sum(test_list)
answer = 0

while start<=end:
    mid = (start+end)//2
    total_score = 0
    cnt = 0

    for score in test_list:
        total_score += score

        if total_score >= mid:
            cnt+=1
            total_score = 0

    if cnt >= K:
        answer = mid
        start = mid + 1
    else:
        end = mid-1

print(answer)