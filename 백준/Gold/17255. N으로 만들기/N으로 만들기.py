import sys
input = sys.stdin.readline

N = str(input()).rstrip()
length = len(N)
check = {}

def dfs(value,path,left,right):
    if right-left + 1 == length and value == N:
        if path not in check.keys():
            check[path] = 1
        return

    if left > 0:
        c = N[left-1]
        temp = c+value
        dfs(c+value,path+temp,left-1,right)

    if right < length -1:
        c = N[right + 1]
        temp = c + value
        dfs(value+c,path+temp,left,right+1)

for i in range(length):
    dfs(N[i],N[i],i,i)

print(len(check.keys()))
