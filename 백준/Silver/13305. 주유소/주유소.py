import sys
input = sys.stdin.readline

if __name__ == '__main__':
    ans = 0
    N = int(input())
    street_len = list(map(int,input().split()))
    city_cost = list(map(int,input().split()))

    c = city_cost[0]

    for i in range(N-1):
        if c > city_cost[i]:
            c = city_cost[i]
        ans += (c*street_len[i])

    print(ans)