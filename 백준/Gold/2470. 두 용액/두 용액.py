import sys
input=sys.stdin.readline

n=int(input())
array=list(map(int,input().split(' ')))
array.sort()
start=0
end=n-1
min = 2e+9+1
result=[0]*2

while end>start:
    left=array[start]
    right=array[end]
    tot=left+right
    if abs(tot)<min:
        min=abs(tot)
        result=[left,right]
    if tot<0:
        start+=1
    else:
        end-=1

print(result[0],result[1])