import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def init_min_tree(tree,start,end,idx):
    if start==end:
        min_tree[idx] = array[start]
        return array[start]
    else:
        mid = (start+end) // 2
        left_data = init_min_tree(tree,start,mid,idx*2)
        right_data = init_min_tree(tree,mid+1,end,idx*2+1)
        min_tree[idx] = min(left_data,right_data)
        return min_tree[idx]

def init_max_tree(tree,start,end,idx):
    if start==end:
        max_tree[idx] = array[start]
        return array[start]
    else:
        mid = (start+end) // 2
        left_data = init_max_tree(tree,start,mid,idx*2)
        right_data = init_max_tree(tree,mid+1,end,idx*2+1)
        max_tree[idx] = max(left_data,right_data)
        return max_tree[idx]

def min_query(tree,start,end,left,right,idx):
    if right<start or left>end:
        return int(1e6)+1
    if left<=start and right>=end:
        return min_tree[idx]

    mid = (start+end) // 2
    left_value = min_query(tree, start, mid, left, right, idx*2)
    right_value = min_query(tree, mid+1, end, left, right, idx * 2+1)
    return min(left_value,right_value)

def max_query(tree,start,end,left,right,idx):
    if right<start or left>end:
        return -1
    if left<=start and right>=end:
        return max_tree[idx]

    mid = (start+end) // 2
    left_value = max_query(tree, start, mid, left, right, idx*2)
    right_value = max_query(tree, mid+1, end, left, right, idx * 2+1)
    return max(left_value,right_value)

if __name__=="__main__":
    N,Q = map(int,input().split())
    array = []
    max_tree = [0] * (N*4)
    min_tree = [0] * (N*4)

    for _ in range(N):
        array.append(int(input()))
    init_min_tree(min_tree,0,N-1,1)
    init_max_tree(max_tree,0,N-1,1)

    for _ in range(Q):
        min_value,max_value = -1,-1
        a,b = map(int,input().split())
        if a == b:
            print(0)
            continue
        min_value = min_query(min_tree,0,N-1,a-1,b-1,1)
        max_value = max_query(max_tree,0,N-1,a-1,b-1,1)
        print(max_value - min_value)