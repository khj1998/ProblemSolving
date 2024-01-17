import sys
input = sys.stdin.readline

c = int(input())

for _ in range(c):
    d,n = map(int,input().split())
    ans = 0
    array = list(map(int,input().split()))
    result = [0]*d
    result[array[0]%d] += 1

    for i in range(1,n):
        array[i] = array[i] + array[i-1]
        result[array[i]%d] += 1

    for i in range(d):
        if i == 0:
            ans += result[i]
        if result[i] > 0:
            ans += (result[i]*(result[i]-1))//2

    print(ans)
