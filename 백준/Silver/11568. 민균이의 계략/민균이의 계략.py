import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())

ans_list = []
array = list(map(int,input().split()))

for x in array:
    if not ans_list:
        ans_list.append(x)
    else:
        idx = bisect_left(ans_list,x)

        if idx == len(ans_list):
            ans_list.append(x)
        else:
            ans_list[idx] = x

print(len(ans_list))