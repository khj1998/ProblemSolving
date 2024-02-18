import sys
input = sys.stdin.readline

N = int(input())
ans = -1
array = []

for _ in range(N):
    array.append(int(input()))
array.sort()

sum_set = set()

for i in array:
    for j in array:
        sum_set.add(i+j)

for i in range(N-1):
    for j in range(i+1,N):
        if array[j] > array[i] and (array[j] - array[i]) in sum_set:
            ans = max(ans,array[j])

print(ans)
