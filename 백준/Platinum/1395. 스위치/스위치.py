import sys
import math
sys.setrecursionlimit(10**4)
input=sys.stdin.readline

n,m=map(int,input().split())
h=math.ceil(math.log2(n))
size=2**h
tree=[0]*size*2
lazy=[0]*size*2


def update_lazy(node,start,end):
    if lazy[node]%2==1:
        tree[node]=(end-start+1)-tree[node]
        if start!=end:
            lazy[node*2]+=lazy[node]
            lazy[node*2+1]+=lazy[node]
        lazy[node]=0


# 스위치가 두번 켜지면 원상태로 돌아간다. 따라서 스위치 키는것은 홀수번일때만 의미가 있다.
def update(node,start,end,left,right):
    update_lazy(node,start,end)
    if start>right or end<left:
        return

    if left<=start and right>=end:
        tree[node]=(end-start+1)-tree[node]
        if start!=end:
            lazy[node*2]+=1
            lazy[node*2+1]+=1
        return

    mid=(start+end)//2
    update(node*2,start,mid,left,right)
    update(node*2+1,mid+1,end,left,right)
    tree[node]=tree[node*2]+tree[node*2+1] # 더해주는걸 왜 빼먹냐....


def query(node,start,end,left,right):
    update_lazy(node,start,end)
    if start>right or end<left:
        return 0
    if left <= start and right >= end:
        return tree[node]
    mid=(start+end)//2
    return query(node*2,start,mid,left,right)+query(node*2+1,mid+1,end,left,right)


for _ in range(m):
    o,s,t=map(int,input().split())

    if o==0:
        update(1,1,n,s,t)
    elif o==1:
        result=query(1,1,n,s,t)
        print(result)