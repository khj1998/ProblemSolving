import sys
input = sys.stdin.readline
import heapq
INF = int(1e8)

n = int(input())
m = int(input())
distance = [INF] * (n+1)
path = [i for i in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

s,e = map(int,input().split())
result = [e]

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        dist,now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for y,cost in graph[now]:
            next_cost = dist + cost

            if distance[y] > next_cost:
                distance[y] = next_cost
                path[y] = now
                heapq.heappush(q,(next_cost,y))

dijkstra(s)
print(distance[e])

while True:
    temp = path[e]
    result.append(temp)

    if temp == s:
        break

    e = path[e]

result.reverse()

print(len(result))

for i in result:
    print(i,end = " ")
