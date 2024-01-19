import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
ans = []

for _ in range(M):
    a,b = map(int,input().split())
    graph[b].append(a)

for i in range(1,N+1):
    check = [False] * (N+1)
    cnt = 1
    check[i]  =True
    q = deque()
    q.append(i)

    while q:
        x = q.popleft()

        for y in graph[x]:
            if not check[y]:
                cnt += 1
                check[y] = True
                q.append(y)

    ans.append((cnt,i))

ans.sort(key = lambda x:(-x[0],x[1]))
max_cnt = ans[0][0]

for cnt,num in ans:
    if cnt == max_cnt:
        print(num,end=" ")
    else:
        break
        