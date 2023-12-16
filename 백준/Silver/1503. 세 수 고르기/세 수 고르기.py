import sys
input = sys.stdin.readline

N,M = map(int,input().split())
ans = int(1e10)
S = list(map(int,input().split()))
check = [False]*(1002)

for s in S:
    check[s] = True

for i in range(1,1001):
    if check[i]:
        continue
    for j in range(i,1001):
        if check[j]:
            continue
        for k in range(j,1002):
            if check[k]:
                continue
            ans = min(ans,abs(N - i*j*k))

print(ans)