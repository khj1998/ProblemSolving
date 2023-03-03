import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

class Node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

def set_node(data,root):
    if data < root:
        if tree[root].left == -1:
            tree[root].left = data
            tree[data] = Node(data,-1,-1)
        else:
            set_node(data,tree[root].left)
    elif data > root:
        if tree[root].right == -1:
            tree[root].right = data
            tree[data] = Node(data, -1, -1)
        else:
            set_node(data,tree[root].right)

def postorder(node):
    if node.left != -1:
        postorder(tree[node.left])
    if node.right != -1:
        postorder(tree[node.right])
    print(node.data)

if __name__=="__main__":
    global tree
    tree = {}
    preorder = []

    while True:
        try:
            preorder.append(int(input()))
        except:
            break

    l = len(preorder)
    root = preorder[0]
    tree[root] = Node(root,-1,-1)

    for i in range(1,l):
        set_node(preorder[i],root)
    postorder(tree[root])
