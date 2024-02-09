import sys
input = sys.stdin.readline

N = int(input())
ans = -1
array = list(map(int,input().split()))

for i in range(1,N):
    array[i] += array[i-1]

def solution(index):
    result = 0
    temp_value = 0
    if index == 0: # 꿀통이 왼쪽에 있을때
        result += (array[N-1] - (array[N-1] - array[N-2]))

        for i in range(1,N-1):
            temp = array[i-1]
            temp_value = max(temp - (array[i] - array[i-1]) , temp_value)

        result += temp_value
    elif index == N-1: # 꿀통이 오른쪽에 있을때
        result += (array[N-1] - array[0])

        for i in range(1,N-1):
            temp = array[N-1] - array[i]
            temp_value = max(temp - (array[i] - array[i-1]),temp_value)

        result += temp_value
    else: # 나머지 위치에 있을때
        result += (array[index] - array[0])
        result += (array[N-2] - array[index-1])

    return result

for i in range(N):
    ans = max(ans,solution(i))

print(ans)
