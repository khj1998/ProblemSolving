import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * V
    distance[start-1] = 0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist,now = heapq.heappop(q)

        if distance[now-1] < dist:
            continue

        for next,cost in graph[now]:
            nextcost = distance[now-1] + cost
            if nextcost < distance[next-1]:
                distance[next-1] = nextcost
                heapq.heappush(q,(nextcost,next))

    return distance

if __name__ =="__main__":
    V,E = map(int,input().split())
    K = int(input())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))

    distance = dijkstra(K)

    for i in distance:
        if i==INF:
            print('INF')
        else:
            print(i)