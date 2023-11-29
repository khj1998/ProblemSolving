import sys
input = sys.stdin.readline

N = int(input())
nodes = list(map(int,input().split()))
del_node = int(input())
start = -1
tree = {}
answer = []

for i in range(N):
    tree[i] = []

for idx,node in enumerate(nodes):
    if node == -1:
        start = idx
        continue

    if idx == del_node or node == del_node:
        continue

    tree[node].append(idx)

def find_leaf(start):
    if not tree[start]:
        answer.append(start)
        return

    for y in tree[start]:
        find_leaf(y)

find_leaf(start)

if del_node == start:
    print(0)
else:
    print(len(answer))