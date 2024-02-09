import sys
input = sys.stdin.readline

N = int(input())
ans = -1
array = list(map(int,input().split()))

def solution(index):
    result = 0
    temp_value = 0
    if index == 0: # 꿀통이 왼쪽에 있을때
        result += (sum(array) - array[N-1])

        for i in range(1,N-1):
            temp = 0
            for j in range(i):
                temp += array[j]

            temp_value = max(temp_value,temp - array[i])

        result += temp_value
    elif index == N-1: # 꿀통이 오른쪽에 있을때
        result += (sum(array) - array[0])

        for i in range(1,N-1):
            temp = 0
            for j in range(i+1,N):
                temp += array[j]

            temp_value = max(temp_value, temp - array[i])

        result += temp_value
    else: # 나머지 위치에 있을때
        for j in range(1,index+1):
            result += array[j]

        for j in range(index,N-1):
            result += array[j]

    return result

for i in range(N):
    ans = max(ans,solution(i))

print(ans)
