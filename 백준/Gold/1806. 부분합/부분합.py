import sys
input = sys.stdin.readline
INF = int(1e9)

N,S = map(int,input().split())
array = list(map(int,input().split()))

if sum(array) < S:
    print(0)
else:
    ans = N
    start, end = 0,0
    result = array[0]

    while start <= N-1:
        if end < N-1 and result < S:
            end += 1
            result += array[end]
        elif result >= S:
            if end == start:
                ans = 1
                break
            ans = min(ans,end-start+1)
            result -= array[start]
            start += 1
        else:
            break

    print(ans)
