import sys
input = sys.stdin.readline

N,K = map(int,input().split())
array = list(map(int,input().split()))
height_diff = []

for i in range(1,len(array)):
    height_diff.append(array[i]-array[i-1])

height_diff.sort()

for _ in range(K-1):
    height_diff.pop()

print(sum(height_diff))
