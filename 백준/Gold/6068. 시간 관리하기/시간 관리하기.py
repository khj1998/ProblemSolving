import sys
input = sys.stdin.readline

N = int(input())
array = []

for _ in range(N):
    T,S = map(int,input().split())
    array.append((T,S))

array.sort(key = lambda x:-x[1])

end_time = array[0][1]
start_time = array[0][1] - array[0][0] + 1

for i in range(1,len(array)):
    t,s = array[i]

    if s >= start_time:
        end_time = start_time - 1
    else:
        end_time = s

    start_time = end_time - t + 1

    if start_time < 0:
        break

if start_time - 1 < 0:
    print(-1)
else:
    print(start_time - 1)