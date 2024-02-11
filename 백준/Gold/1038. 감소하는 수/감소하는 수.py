import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
numbers = [i for i in range(10)]
array = []

for i in range(1,11):
    for j in list(combinations(numbers,i)):
        j = sorted(j,reverse=True)
        array.append(int("".join(map(str,j))))

try:
    array.sort()
    print(array[N])
except:
    print(-1)
