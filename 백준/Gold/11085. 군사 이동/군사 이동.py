import sys
import heapq
input=sys.stdin.readline

p,w=map(int,input().split())
c,v=map(int,input().split())
parent=[0]*p
for i in range(p):
    parent[i]=i

q=[]
for _ in range(w):
    a,b,C=map(int,input().split())
    heapq.heappush(q,(-C,a,b))

def find(parent,a):
    if parent[a]!=a:
        parent[a]=find(parent,parent[a])
    return parent[a]

def union(parent,a,b):
    a=find(parent,a)
    b=find(parent,b)

    if a>b:
        parent[b]=a
    else:
        parent[a]=b

ans=-1

while q:
    cost,x,y=heapq.heappop(q)
    cost=-cost

    union(parent,x,y)

    if find(parent,c)==find(parent,v):
        ans=cost
        break

print(ans)