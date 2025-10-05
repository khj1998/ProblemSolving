from collections import defaultdict, deque

def solution(edges):
    answer = [0, 0, 0, 0]
    
    in_out_degree = defaultdict(lambda: [0, 0])
    graph = defaultdict(list)
    
    nodes = set()
    for u, v in edges:
        in_out_degree[u][1] += 1
        in_out_degree[v][0] += 1
        nodes.add(u)
        nodes.add(v)
        graph[u].append(v)

    for node in nodes:
        if in_out_degree[node][0] == 0 and in_out_degree[node][1] >= 2:
            generated_node = node
            answer[0] = generated_node
            break
            
    visited = set()
    visited.add(generated_node)
    
    for start_node in graph[generated_node]:
        if start_node in visited:
            continue
    
        q = deque([start_node]) 
        visited.add(start_node)
        
        vertex_count = 0
        edge_count = 0
        
        while q:
            curr = q.popleft()
            vertex_count += 1
            edge_count += in_out_degree[curr][1]
            
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

        if vertex_count == edge_count:
            answer[1] += 1
        elif vertex_count > edge_count:
            answer[2] += 1
        else:
            answer[3] += 1
            
    return answer