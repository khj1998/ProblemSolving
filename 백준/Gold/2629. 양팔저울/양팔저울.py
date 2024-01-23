import sys
input = sys.stdin.readline

N = int(input())
chu_list = list(map(int,input().split()))
M = int(input())
ball_list = list(map(int,input().split()))
dp = [[False]*(15001) for _ in range(31)]

def recursive_dp(index,value):
    if index > N:
        return

    if dp[index][value]:
        return

    dp[index][value] = True

    recursive_dp(index+1,value+chu_list[index-1])
    recursive_dp(index+1,abs(value-chu_list[index-1]))
    recursive_dp(index+1,value)

recursive_dp(0,0)

for i in ball_list:
    if i> 15000:
        print('N',end=" ")
        continue
    if dp[N][i]:
        print('Y',end=" ")
    else:
        print('N',end=" ")

