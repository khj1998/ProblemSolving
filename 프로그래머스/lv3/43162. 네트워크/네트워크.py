def dfs(x,check,graph):
    check[x] = True
    
    for y in graph[x]:
        if not check[y]:
            dfs(y,check,graph)

def solution(n, computers):
    answer = 0
    check = [False]*n
    graph=[[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j] == 1:
                graph[i].append(j)
    
    for i in range(n):
        if not check[i]:
            dfs(i,check,graph)
            answer+=1
    
    return answer