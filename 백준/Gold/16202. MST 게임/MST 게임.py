import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(x):
    if parent[x]!=x:
        x = find(parent[x])
    return x

def union(x,y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

if __name__ =="__main__":
    n,m,k = map(int,input().split())
    edges = []
    ans = []
    cost = 1

    for _ in range(m):
        x,y = map(int,input().split())
        edges.append((x,y,cost))
        cost+=1

    for _ in range(k):
        parent = [i for i in range(n + 1)]
        edges.sort(key=lambda x: x[2])
        V = 0
        score = 0

        for x,y,cost in edges:
            if V == n-1:
                break

            if find(x)!=find(y):
                union(x,y)
                score += cost
                V+=1

        if V!=n-1:
            ans.append(0)
        else:
            ans.append(score)

        edges.pop(0)

    for i in ans:
        print(i,end=" ")