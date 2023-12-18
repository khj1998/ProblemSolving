import sys
input = sys.stdin.readline
import heapq

ans = 0
N,M = map(int,input().split())
tree = [[] for _ in range(N+1)]
INF = int(1e9)
fox_distance = [INF]*(N+1)
wolf_distance = [[INF]*2 for _ in range(N+1)]

for _ in range(M):
    a,b,d = map(int,input().split())
    d*=2

    tree[a].append((b,d))
    tree[b].append((a,d))

def get_fox_distance(start):
    fox_distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist,now = heapq.heappop(q)

        if fox_distance[now] < dist:
            continue

        for next,cost in tree[now]:
            next_cost = cost + dist

            if next_cost < fox_distance[next]:
                fox_distance[next] = next_cost
                heapq.heappush(q,(next_cost,next))

def get_wolf_distance(start):
    wolf_distance[start][0] = 0
    q = []
    heapq.heappush(q,(0,False,start))

    while q:
        dist,is_double,now = heapq.heappop(q)

        if wolf_distance[now][is_double] < dist:
            continue

        for next,cost in tree[now]:
            next_cost = 0

            if is_double:
                next_cost = dist + cost*2
            else:
                next_cost = dist + cost//2

            if wolf_distance[next][not is_double] > next_cost:
                wolf_distance[next][not is_double] = next_cost
                heapq.heappush(q,(next_cost,not is_double,next))

get_fox_distance(1)
get_wolf_distance(1)

for i in range(2,N+1):
    fox_cost,wolf_cost = fox_distance[i],min(wolf_distance[i])

    if fox_cost < wolf_cost:
        ans += 1

print(ans)