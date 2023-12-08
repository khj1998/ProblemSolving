import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
bugs = str(input()).rstrip()
tree = [[] for _ in range(N+1)]
parent = [[] for _ in range(N+1)]
X,Y = map(int,input().split())
node_position = defaultdict(list)
tree_level = [0] * (N+1)
node = 1
recent_node = []
dead_apple = []

def set_tree_level(x,level):
    tree_level[x] = level

    for y in tree[x]:
        set_tree_level(y,level+1)

for idx,i in enumerate(bugs):

    if i == '0':
        if idx+1 in [X,Y]:
            dead_apple.append(node)

        node_position[node] = [idx + 1]

        if not recent_node:
            recent_node.append(node)
        else:
            tree[recent_node[-1]].append(node)
            recent_node.append(node)
        node+=1
    else:
        pop_node = recent_node.pop()
        node_position[pop_node].append(idx+1)

        if idx + 1 in [X, Y]:
            dead_apple.append(pop_node)

set_tree_level(1,1)

min_level = min(tree_level[dead_apple[0]],tree_level[dead_apple[1]])
max_lv,ans = -1,[]

for i in range(1,N+1):
    child_node = []
    if tree_level[i] > max_lv and tree_level[i] <= min_level:
        stack = [i]

        while stack:
            x = stack.pop()

            if x in dead_apple:
                child_node.append(x)

            for y in tree[x]:
                stack.append(y)

        if dead_apple[0] in child_node and dead_apple[1] in child_node:
            max_lv = max(max_lv,tree_level[i])
            ans = node_position[i]

for x in ans:
    print(x,end = " ")