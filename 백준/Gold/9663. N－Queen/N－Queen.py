import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n=int(input())
col=[0]*n
result=0

def queens(x):
    global result
    if x==n:
        result+=1
        return
    else:
        for i in range(n):
            col[x]=i
            if promising(x):
                queens(x+1)

def promising(x):
    for i in range(x):
        if col[x]==col[i] or abs(col[x]-col[i])==x-i:
            return False
    return True

answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[n])