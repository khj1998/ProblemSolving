import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
array = list(map(int,input().split()))
ans_list = []

for x in array:
    if not ans_list:
        ans_list.append(x)

    if ans_list[-1] < x:
        ans_list.append(x)
    else:
        idx = bisect_left(ans_list,x)
        ans_list[idx] = x

print(len(ans_list))