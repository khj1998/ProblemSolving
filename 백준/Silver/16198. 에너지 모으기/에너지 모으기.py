import sys
input = sys.stdin.readline
from copy import deepcopy

N = int(input())
ans = []
array = list(map(int,input().split()))

def dfs(left,right,value,array):
    if right - left - 1 == 1:
        ans.append(value)
        return

    for i in range(left+1,right-1):
        temp = deepcopy(array)
        temp_value = temp[i-1]*temp[i+1]
        temp.pop(i)
        dfs(0,len(temp),value+temp_value,temp)

dfs(0,N,0,array)
ans.sort(reverse = True)
print(ans[0])
