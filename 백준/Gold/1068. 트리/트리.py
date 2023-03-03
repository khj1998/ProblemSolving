import sys
input = sys.stdin.readline

def find_root(node_list):
    ans = -1
    l = len(node_list)
    for node_num in range(l):
        if node_list[node_num] == -1:
            ans = node_num
            break;
    return ans

def init_tree(tree,node_list):
    l = len(node_list)
    for node_num in range(l):
        if node_list[node_num] == -1:
            continue
        else:
            tree[node_num].append(node_list[node_num])
            tree[node_list[node_num]].append(node_num)

def get_leaf_node(root):
    check[root] = True
    has_child = False

    for child in tree[root]:
        if child==del_node:
            continue
        elif check[child] == False:
            has_child = True
            get_leaf_node(child)

    if not has_child:
        ans_list.append(root)

if __name__=="__main__":
    N = int(input())
    ans_list = []
    tree = [[] for _ in range(N)]
    check = [False]*N
    node_list = list(map(int,input().split()))
    del_node = int(input())
    init_tree(tree,node_list)
    root = find_root(node_list)
    if del_node == root:
        print(0)
    else:
        get_leaf_node(root)
        print(len(ans_list))