import sys
input = sys.stdin.readline

N,M = map(int,input().split())
connect_edge_count = 0
duplicate_edge_count = 0
parent = [i for i in range(N+1)]

def find(a):
    if parent[a]!=a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    a,b = map(int,input().split())

    if find(a)!=find(b):
        union(a,b)
        connect_edge_count += 1
    else:
        duplicate_edge_count += 1

print(N-1-connect_edge_count + duplicate_edge_count)
