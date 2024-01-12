import sys
input = sys.stdin.readline

while True:
    n,m = map(float,input().split())
    candies = []

    if n==0 and m==0.00:
        break

    max_money = int(m*100)
    dp = [0] * (max_money+1)

    for _ in range(int(n)):
        c,p = map(float,input().split())
        candies.append((int(p*100 + 0.5),int(c)))

    candies.sort()

    for i in range(1,max_money+1):
        for p,c in candies:
            if p > i:
                break
            dp[i] = max(dp[i],c + dp[i-p])

    print(max(dp))
