import sys
import math
from itertools import combinations
input=sys.stdin.readline

n=int(input())
array=[]
result_min=1000000001

for _ in range(n):
    array.append(list(map(int,input().split())))

people=list(range(n))
candidate=list(combinations(people,n//2))

for group in candidate:
    rest=list(set(people)-set(group))
    rest_sum=0
    group_sum=0

    rest_combination=list(combinations(rest,2))
    group_combination=list(combinations(list(group),2))

    for x,y in rest_combination:
        rest_sum+=array[x][y]+array[y][x]

    for x,y in group_combination:
        group_sum+=array[x][y]+array[y][x]

    if result_min>abs(rest_sum-group_sum):
        result_min=abs(rest_sum-group_sum)

print(result_min)