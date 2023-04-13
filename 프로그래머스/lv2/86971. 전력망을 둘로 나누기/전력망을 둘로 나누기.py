def dfs(start,banned):
    check[start] = True
    ans = 0
    node_list.append(start)
    
    for next_v in graph[start]:
        if next_v == banned:
            continue
        if not check[next_v]:
            dfs(next_v,banned)

def solution(n, wires):
    global graph,check,node_list
    answer = int(1e5)
    graph = [[] for _ in range(n+1)]
    
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    # 매 wires 제거하면 결과 비교
    for v1,v2 in wires:
        check = [False]*(n+1)
        node_list = []
        dfs(v1,v2)
        ans1 = len(node_list)
        node_list.clear()
        dfs(v2,v1)
        ans2 = len(node_list)
        answer = min(answer,abs(ans1-ans2))
        
    return answer