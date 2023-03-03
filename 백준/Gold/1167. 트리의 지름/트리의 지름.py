import sys
input = sys.stdin.readline
from collections import deque

def find_root(start):
    q = deque()
    q.append((0,start))
    ans = []
    check = [False] * (V + 1)

    while q:
        dist,x = q.popleft()
        has_vertex = False
        check[x] = True
        for next,cost in graph[x]:
            if check[next]:
                continue
            else:
                has_vertex = True
                q.append((dist+cost,next))
        if has_vertex == False:
            ans.append((dist,x))
    ans = sorted(ans,key=lambda x:-x[0])
    return ans[0][1]

def find_diameter(start,ans_list):
    q = deque()
    q.append((0,start))
    check = [False] * (V + 1)

    while q:
        dist,now = q.popleft()
        check[now] = True
        has_vertex = False
        for next,cost in graph[now]:
            if check[next]:
                continue
            else:
                has_vertex = True
                q.append((dist+cost,next))
        if has_vertex == False:
            ans_list.append(dist)

if __name__=="__main__":
    V = int(input())
    ans_list = []
    graph = [[] for _ in range(V+1)]

    for _ in range(V):
        vertex = list(map(int,input().split()))
        now_vertex = vertex[0]
        l = len(vertex)
        for idx in range(1,l//2):
            graph[vertex[0]].append([vertex[idx*2-1],vertex[idx*2]])

    node = find_root(1)
    find_diameter(node,ans_list)
    print(max(ans_list))
