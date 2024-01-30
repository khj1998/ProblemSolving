import sys
input = sys.stdin.readline

n = int(input())
ans = 0
day_check = [False]*(10001)
day_check[0] = True
array = []

for _ in range(n):
    p,d = map(int,input().split())
    array.append((p,d))

array.sort(key = lambda x:-x[0])

for p,d in array:
    if not day_check[d]:
        ans += p
        day_check[d] = True
    else:
        d -= 1
        while d >= 1:
            if not day_check[d]:
                ans += p
                day_check[d] = True
                break
            d-=1

print(ans)
