import sys
input = sys.stdin.readline
from itertools import product

N,K = map(int,input().split())
array = list(map(int,input().split()))
iters = len(str(N))
Product = []
total_number = []

for i in range(1,iters+1):
    Product += list(product(array,repeat = i))

for x in Product:
    y = ''
    for i in x:
        y += str(i)
    total_number.append(int(y))

total_number.sort(reverse=True)

for x in total_number:
    if x<=N:
        print(x)
        break