import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

class Node:
    def __init__(self,root,left,right):
        self.root=root
        self.left=left
        self.right=right

def postorder(node):
    if node==None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.root)

def find_idx(preorder,pstart,root,size):
    i=pstart
    count=0
    while count<size:
        if root>=preorder[i]:
            count+=1
            i+=1
        else:
            return i
    return -1

def find_tree(preorder,pstart,size):
    if size<=0:
        return None
    root=preorder[pstart]
    idx=find_idx(preorder,pstart,root,size)
    if idx==-1:
        leftsize=size-1
        rightsize=0
    else:
        leftsize = idx - pstart - 1
        rightsize = size - leftsize - 1
    left=find_tree(preorder,pstart+1,leftsize)
    right=find_tree(preorder,idx,rightsize)
    return Node(root=root,left=left,right=right)

if __name__=='__main__':
    preorder=[]
    while True:
        try:
            num=int(input())
            preorder.append(num)
        except:
            break
    tree=find_tree(preorder,0,len(preorder))
    postorder(tree)