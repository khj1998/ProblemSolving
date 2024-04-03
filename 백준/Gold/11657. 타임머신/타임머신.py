import sys
input=sys.stdin.readline
INF=int(1e9)

N,M=map(int,input().split())
graph=[]
distance=[1e9]*(N+1)
for _ in range(M):
    a,b,c=map(int,input().split())
    graph.append((a,b,c))

def bf(start):
    distance[start]=0
    for i in range(N):
        for j in range(M):
            now=graph[j][0]
            next=graph[j][1]
            cost=graph[j][2]
            dist=distance[now]+cost
            if distance[now]!=INF and distance[next]>dist:
                distance[next]=dist
                if i==N-1:
                    return True
    return False

negative=bf(1)

if negative:
    print(-1)
else:
  for i in range(2,N+1):
     if distance[i]==INF:
         print(-1)
     else:
         print(distance[i])