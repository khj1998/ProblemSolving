import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)

n,m,k=map(int,input().split())
distance=[[INF]*k for _ in range(n+1)]
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])

def dijkstra(start):
    q=[]
    distance[1][0]=0
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)

        for next,cost in graph[now]:
            next_cost=dist+cost
            if distance[next][k-1]>next_cost:
                distance[next][k-1]=next_cost
                distance[next].sort()
                heapq.heappush(q,(next_cost,next))

dijkstra(1)

for i in range(1,n+1):
    if distance[i][k-1]==INF:
        print(-1)
    else:
        print(distance[i][k-1])