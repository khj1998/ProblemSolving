import sys
input = sys.stdin.readline

if __name__=="__main__":
    N, M = map(int, input().split())
    ans = 0
    max_dist = 0
    array = list(map(int, input().split()))
    plus,minus = [],[]

    for i in array:
        max_dist  = max(max_dist,abs(i))
        if i > 0:
            plus.append(i)
        else:
            minus.append(abs(i))

    plus.sort(reverse = True)
    minus.sort(reverse = True)

    for i in range(0,len(plus),M):
        ans += plus[i]*2

    for i in range(0,len(minus),M):
        ans += minus[i]*2

    print(ans - max_dist)
