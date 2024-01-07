import sys
input = sys.stdin.readline
import heapq

N = int(input())
K = int(input())
array = list(map(int,input().split()))
array.sort()

if len(array) <= K:
    print(0)
else:
    sensor_dist = []

    for i in range(1,len(array)):
        sensor_dist.append(array[i] - array[i-1])

    sensor_dist.sort()

    for _ in range(K-1):
        sensor_dist.pop()

    print(sum(sensor_dist))
