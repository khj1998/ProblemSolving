import sys
from itertools import combinations
from collections import deque

def check_min(choice):
    distance = 0

    for house in houses:
        house_dist = int(1e9)
        for c in choice:
            dist = abs(house[0]-c[0]) + abs(house[1]-c[1])
            house_dist = min(house_dist,dist)
        distance+=house_dist
    return distance

if __name__ =="__main__":
    N,M = map(int,input().split())
    graph = []
    houses = []
    chickens = []
    ans = int(1e9)

    for _ in range(N):
        graph.append(list(map(int,input().split())))

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                houses.append((i,j))
            elif graph[i][j] == 2:
                chickens.append((i,j))

    choices = list(combinations(chickens,M))

    for choice in choices:
        ans = min(ans,check_min(choice))

    print(ans)