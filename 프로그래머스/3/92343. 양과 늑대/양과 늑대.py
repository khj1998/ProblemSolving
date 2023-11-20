from collections import defaultdict

def set_parent_child(edges):
    tree = defaultdict(list)
        
    for edge in edges:
        if edge[0] not in tree.keys():
            tree[edge[0]] = [edge[1]]
        else:
            tree[edge[0]].append(edge[1])
        
    return tree

def get_sheep_max(info,next_nodes,tree,sheep_num,wolf_num):
    if not next_nodes:
        return sheep_num
    
    max_num = sheep_num
    
    for idx,x in enumerate(next_nodes):
        if info[x] == 0:
            max_num = max(max_num,get_sheep_max(info,next_nodes[:idx]+next_nodes[idx+1:]+tree[x],tree,sheep_num+1,wolf_num))
        elif sheep_num > wolf_num + 1:
            max_num = max(max_num,get_sheep_max(info,next_nodes[:idx]+next_nodes[idx+1:]+tree[x],tree,sheep_num,wolf_num+1))
    
    return max_num

def solution(info, edges):
    answer = 0
    tree = set_parent_child(edges)
    
    return get_sheep_max(info,[0],tree,0,0)