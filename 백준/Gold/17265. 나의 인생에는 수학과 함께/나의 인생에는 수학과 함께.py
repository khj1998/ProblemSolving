import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
INF = int(1e8)
q = deque()
dx,dy = [0,1],[1,0]
dic = {}
graph = []

for _ in range(N):
    s = str(input()).rstrip()
    graph.append(s.split(' '))

def update(is_max):
    dp = []
    q = deque()

    if is_max:
        dp = [[-INF]*N for _ in range(N)]
    else:
        dp = [[INF]*N for _ in range(N)]

    dp[0][0] = int(graph[0][0])
    q.append((0,0,dp[0][0]))

    while q:
        x,y,value = q.popleft()

        for i in range(2):
            px,py = x+dx[i],y+dy[i]

            if 0<=px<N and 0<=py<N:
                if 48 <= ord(graph[px][py]) <= 53:
                    result = 0

                    if graph[x][y] == '*':
                        result = value * int(graph[px][py])
                    elif graph[x][y] == '-':
                        result = value - int(graph[px][py])
                    elif graph[x][y] == '+':
                        result = value + int(graph[px][py])

                    if is_max and dp[px][py] < result:
                        dp[px][py] = result
                        q.append((px,py,result))
                    elif not is_max and dp[px][py] > result:
                        dp[px][py] = result
                        q.append((px,py,result))
                else:
                    if is_max and dp[px][py] < value:
                        dp[px][py] = value
                        q.append((px,py,value))
                    elif not is_max and dp[px][py] > value:
                        dp[px][py] = value
                        q.append((px, py, value))

    return dp[N-1][N-1]

print(update(True),update(False))
