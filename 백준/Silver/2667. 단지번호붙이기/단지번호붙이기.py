import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(x, y):
    if (x >= n or x < 0)or (y >= n or y < 0) or (arr[x][y] == '0'):
        return
    global t
    arr[x][y] = '0'
    t += 1
    dfs(x+1, y)
    dfs(x, y+1)
    dfs(x-1, y)
    dfs(x, y-1)

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(input()))

h = 0
hl = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            t = 0
            dfs(i, j)
            h += 1
            hl.append(t)
print(h)
hl.sort()
for i in hl:
    print(i)