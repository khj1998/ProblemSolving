import sys
input = sys.stdin.readline
from collections import deque
INF = int(1e8)

def find_min_cost():
    q = deque()
    check = [[INF]*N for _ in range(N)]
    check[0][0] = graph[0][0]
    q.append((0,0))

    while q:
        x,y = q.popleft()

        for i in range(4):
            px = x+dx[i]
            py = y+dy[i]

            if 0<=px<N and 0<=py<N:
                if check[px][py] > check[x][y] + graph[px][py]:
                    check[px][py] = check[x][y] + graph[px][py]
                    q.append((px,py))

    return check[N-1][N-1]

if __name__ =="__main__":
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    problem = 1

    while True:
        N = int(input())

        if N==0:
            break

        graph = []
        for _ in range(N):
            graph.append(list(map(int,input().split())))

        ans = find_min_cost()
        print("Problem {0}: {1}".format(problem,ans))
        problem+=1