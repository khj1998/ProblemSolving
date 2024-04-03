import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
arr=[0]*(n+1)
tree=[0]*(n+1)
answer=[]

def update(i,dif):
    while i<=n:
        tree[i]+=dif
        i+=(i&-i)

def prefix_sum(i):
    result=0
    while i>0:
        result+=tree[i]
        i-=(i&-i)
    return result

def interval_sum(start,end):
    return prefix_sum(end)-prefix_sum(start-1)

for i in range(1,n+1):
    x=int(input())
    arr[i]=x
    update(i,x)

for i in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        update(b,c-arr[b])
        arr[b]=c
    else:
        answer.append(interval_sum(b,c))

for i in range(len(answer)):
    print(answer[i])