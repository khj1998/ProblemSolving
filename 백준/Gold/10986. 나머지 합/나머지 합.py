import sys
input = sys.stdin.readline

N,M = map(int,input().split())
array = list(map(int,input().split()))
ans,prefix_sum = 0,0
divide = [0]*M

for i in array:
    prefix_sum+=i
    x = prefix_sum % M
    divide[x] +=1

    if x == 0:
        ans += 1

for i in divide:
    ans += (i * (i-1))//2

print(ans)