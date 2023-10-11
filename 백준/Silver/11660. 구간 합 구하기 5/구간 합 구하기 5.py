import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N,M = map(int,input().split())
    graph = [[0] * (N+1)]

    for _ in range(N):
        graph.append([0] + list(map(int,input().split())))

    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j] = graph[i][j] + graph[i][j-1] + graph[i-1][j] - graph[i-1][j-1]

    for _ in range(M):
        x1,y1,x2,y2 = map(int,input().split())

        print(graph[x2][y2]-graph[x2][y1-1]-graph[x1-1][y2]+graph[x1-1][y1-1])