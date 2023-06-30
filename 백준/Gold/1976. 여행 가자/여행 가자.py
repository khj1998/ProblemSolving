import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input())
m=int(input())
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i

def find_parent(parent,a):
    if a!=parent[a]:
        a=find_parent(parent,parent[a])
    return parent[a]

def union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(1,n+1):
    path=list(map(int,input().split()))
    for j in range(len(path)):
        if path[j]==1:
            union(parent,i,j+1)

plan=list(map(int,input().split()))
result=set([find_parent(parent,i) for i in plan])
if len(result)==1:
    print("YES")
else:
    print("NO")