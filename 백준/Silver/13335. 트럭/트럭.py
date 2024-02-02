import sys
input = sys.stdin.readline

n,w,L = map(int,input().split())
array = list(map(int,input().split()))
ans = 0
bridge = [0] * w

while bridge:
    ans += 1
    bridge.pop(0)

    if array:
        if (sum(bridge)) + array[0] <= L:
            bridge.append(array.pop(0))
        else:
            bridge.append(0)

print(ans)
