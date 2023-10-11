from collections import deque
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    N,K = map(int,input().split())
    q = deque()
    virus = []
    graph = []

    for _ in range(N):
        graph.append(list(map(int,input().split())))

    S,X,Y = map(int,input().split())

    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                virus.append((graph[i][j],i,j,0))

    virus.sort(key = lambda x:x[0])

    for v in virus:
        q.append(v)

    while q:
        virus_num,x,y,s = q.popleft()

        if s >= S:
            break

        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]

            if 0<=px<N and 0<=py<N and graph[px][py] == 0:
                graph[px][py] = virus_num
                q.append((virus_num,px,py,s+1))

    if graph[X-1][Y-1]:
        print(graph[X-1][Y-1])
    else:
        print(0)