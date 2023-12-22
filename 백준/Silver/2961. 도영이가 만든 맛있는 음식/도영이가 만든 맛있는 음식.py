import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
ans = int(1e10)
ingredients = []
temp = [i for i in range(N)]

for _ in range(N):
    a,b = map(int,input().split())
    ingredients.append((a,b))

for i in range(1,N+1):
    total = list(combinations(temp,i))

    for t in total:
        sin, sun = 1, 0
        for j in t:
            sin*=ingredients[j][0]
            sun+=ingredients[j][1]

        ans = min(ans, abs(sin - sun))

print(ans)