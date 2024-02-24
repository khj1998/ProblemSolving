import sys
input = sys.stdin.readline
from itertools import combinations

N,L,R,X = map(int,input().split())
array = list(map(int,input().split()))
ans = 0

if N==1:
    print(0)
else:
    for i in range(2,N+1):
        combination = list(combinations(array,i))

        for comb in combination:
            if L<=sum(comb)<=R and max(comb) - min(comb) >= X:
                ans += 1

    print(ans)