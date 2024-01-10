import sys
input = sys.stdin.readline
from collections import deque
INF = int(1e9)

N,R = map(int,input().split())
check = [False] * N
tree = [[] for _ in range(N)]
distance = [INF] * N
giga_check = False

for _ in range(N-1):
    a,b,d = map(int,input().split())
    tree[a-1].append((b-1,d))
    tree[b-1].append((a-1,d))

def bfs(start):
    global giga_check
    q = deque()
    q.append((start,0))
    distance[start] = 0
    check[start] = True
    giga_node = -1

    while q:
        cnt = 0
        now,dist = q.popleft()

        for next,cost in tree[now]:
            if not check[next]:
                check[next] = True
                distance[next] = dist + cost
                q.append((next,dist+cost))
                cnt+=1

        if not giga_check and cnt >= 2:
            giga_check = True
            giga_node = now

    return giga_node

giga_node = bfs(R-1)

if giga_node == -1:
    max_dist = max(distance)
    print(max_dist - distance[R-1],0)
else:
    max_dist = max(distance)
    print(distance[giga_node] - distance[R-1],max_dist - distance[giga_node])
