import sys
input = sys.stdin.readline

N,K = map(int,input().split())
array = list(map(int,input().split()))
ans = 0
odd,even,end = 0,0,0

for i in range(N):
    start = i

    while end <= N-1 and start <= end:
        if array[end]%2:
            odd+=1
        else:
            even+=1

        if odd == K+1:
            break
        end += 1

    if end == N:
        end-=1

    ans = max(ans,end-start+1-odd)

    if array[start]%2:
        odd-=1
    else:
        even-=1

    if array[end]%2:
        odd-=1
    else:
        even-=1

print(ans)