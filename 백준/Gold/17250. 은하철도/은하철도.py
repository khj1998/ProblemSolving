from collections import deque
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find_parent(x):
    if parent[x]!=x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b):
    x = find_parent(a)
    y = find_parent(b)

    min_root = min(x, y)
    star_num[min_root] = star_num[x] + star_num[y]
    print(star_num[min_root])

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

if __name__ == '__main__':
    N,M = map(int,input().split())
    edges = []

    parent = [i for i in range(N+1)]
    check = [False]*(N+1)
    star_num = [0 for _ in range(N+1)]

    for i in range(1,N+1):
        a = int(input())
        star_num[i] = a

    for _ in range(M):
        a,b = map(int,input().split())
        edges.append((a,b))

    for a,b in edges:
        if find_parent(a) != find_parent(b):
            union(a,b)
        else:
            print(star_num[find_parent(a)])