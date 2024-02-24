import sys
input = sys.stdin.readline

N,M,k = map(int,input().split())
ans = 0
cost_list = [0] + list(map(int,input().split()))
parent = [i for i in range(N+1)]
check = [False] * (N+1)

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x,y):
    x = find_parent(x)
    y = find_parent(y)

    if cost_list[x] > cost_list[y]:
        parent[x] = parent[y]
    else:
        parent[y] = parent[x]

for _ in range(M):
    a,b = map(int,input().split())

    if find_parent(a) != find_parent(b):
        union(a,b)

for i in range(1,N+1):
    root = find_parent(i)
    if not check[root]:
        ans += cost_list[root]
        check[root] = True

if ans > k:
    print('Oh no')
else:
    print(ans)
