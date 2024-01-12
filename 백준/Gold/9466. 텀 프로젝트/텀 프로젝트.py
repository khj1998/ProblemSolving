import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

T=int(input())


def dfs(x):
    global result
    team.append(x)
    check[x]=True

    if check[array[x]]==1:
        if array[x] in team:
            result+=team[team.index(array[x]):]
            return
    else:
        dfs(array[x])


for _ in range(T):
    n=int(input())
    array=[0]
    array+=list(map(int,input().split()))
    check=[False]*(n+1)
    result=[]

    for i in range(1,n+1):
        if not check[i]:
            team = []
            dfs(i)

    print(n-len(result))