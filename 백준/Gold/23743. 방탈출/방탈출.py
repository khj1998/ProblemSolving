import sys
input = sys.stdin.readline
sys.setrecursionlimit((10**5)*3)

def find_parent(x):
    if parent[x]!=x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x,y):
    x,y = find_parent(x),find_parent(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

if __name__=="__main__":
    N,M = map(int,input().split())
    ans = 0
    dic = {}
    parent = [i for i in range(N+1)]
    escape_cost = [0]
    edges = []

    for _ in range(M):
        a,b,c = map(int,input().split())
        edges.append((a,b,c))

    escape_cost += list(map(int,input().split()))

    for i in range(1,len(escape_cost)):
        edges.append((0,i,escape_cost[i]))

    edges.sort(key = lambda x:x[2])

    for x,y,c in edges:
        if find_parent(x) != find_parent(y):
            union(x,y)
            ans += c

    print(ans)
