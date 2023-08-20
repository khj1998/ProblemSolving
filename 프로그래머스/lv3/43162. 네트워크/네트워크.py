def find(parent,x):
    if x!=parent[x]:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,x,y):
    x = find(parent,x)
    y = find(parent,y)
    
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

def solution(n, computers):
    answer = 0
    dic = {}
    parent = [i for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] and find(parent,i)!=find(parent,j):
                union(parent,i,j)
    
    return len(set([find(parent, i) for i in range(n)]))