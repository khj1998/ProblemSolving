import sys
input = sys.stdin.readline

N = int(input())
buildings = list(map(int,input().split()))

def check_max():
    ans = [0] * N

    for i in range(N):
        temp = 0
        inclination_max = -float((int(1e8) * 21))
        x1,y1 = i,buildings[i]

        for j in range(i+1,N):
            temp_inclination = (y1-buildings[j])/(x1-j)

            if temp_inclination > inclination_max:
                temp += 1
                inclination_max = temp_inclination

        ans[i] += temp

    for i in range(N):
        temp = 0
        inclination_min = float((int(1e8) * 21))
        x1,y1 = i,buildings[i]

        for j in range(i-1,-1,-1):
            temp_inclination = (y1-buildings[j])/(x1-j)

            if temp_inclination < inclination_min:
                temp += 1
                inclination_min = temp_inclination

        ans[i] += temp

    return max(ans)

print(check_max())
