import sys
input = sys.stdin.readline
from itertools import combinations

#주어진 2의 치킨 거리를 각각 계산
N,M = map(int,input().split())
dx,dy = [-1,1,0,0],[0,0,-1,1]
INF = int(1e8)
ans = INF
graph = []
houses = []
chicken_list = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken_list.append((i,j))
        elif graph[i][j] == 1:
            houses.append((i,j))

combination = list(combinations(chicken_list,M))

def get_min_value(comb,houses):
    result = 0

    for x,y in houses:
        temp = INF

        for px,py in comb:
            temp = min(temp,abs(x-px)+abs(y-py))
        result += temp

    return result

for comb in combination:
    ans = min(ans,get_min_value(comb,houses))

print(ans)
