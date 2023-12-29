import sys
input = sys.stdin.readline
import heapq

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [int(1e9)]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

s,t = map(int,input().split())

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        dist,now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for next,cost in graph[now]:
            next_cost = cost + dist

            if next_cost < distance[next]:
                distance[next] = next_cost
                heapq.heappush(q,(next_cost,next))

dijkstra(s)
print(distance[t])
