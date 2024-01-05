import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while q:
        x1,y1,x2,y2,cnt = q.popleft()

        if cnt >= 10:
            return -1

        for i in range(4):
            X1,Y1 = x1+dx[i],y1+dy[i]
            X2,Y2 = x2+dx[i],y2+dy[i]

            if (0<=X1<n and 0<=Y1<m) and (0<=X2<n and 0<=Y2<m):
                if graph[X1][Y1] == '#':
                    X1,Y1 = x1,y1
                if graph[X2][Y2] == '#':
                    X2,Y2 = x2,y2
                q.append((X1,Y1,X2,Y2,cnt+1))
            elif (0<=X1<n and 0<=Y1<m):
                return cnt+1
            elif (0<=X2<n and 0<=Y2<m):
                return cnt+1
            else:
                continue

if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    n, m = map(int, input().split())
    q = deque()
    graph = []
    temp = []

    for _ in range(n):
        graph.append(str(input()).rstrip())

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'o':
                temp.append((i,j))

    q.append((temp[0][0],temp[0][1],temp[1][0],temp[1][1],0))
    print(bfs())
