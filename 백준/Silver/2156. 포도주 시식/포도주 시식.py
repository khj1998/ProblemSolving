import sys
input = sys.stdin.readline

if __name__ =="__main__":
    n = int(input())
    array = [0]
    dp = [0] * (n+1)

    for _ in range(n):
        array.append(int(input()))

    if n==1:
        print(array[1])
    elif n==2:
        print(array[1]+array[2])
    else:
        dp[1] = array[1]
        dp[2] = array[1] + array[2]
        for i in range(3,n+1):
            tmp1 = array[i]+array[i-1]+dp[i-3]
            tmp2 = array[i]+dp[i-2]
            tmp3 = dp[i-1]
            dp[i] = max(tmp1,tmp2,tmp3)
        print(dp[n])