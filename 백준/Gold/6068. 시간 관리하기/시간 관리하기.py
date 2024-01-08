import sys
input = sys.stdin.readline

N = int(input())
times = []
start_time = 0

for _ in range(N):
    t,s = map(int,input().split())
    times.append((t,s))

times.sort(key = lambda x:-x[1])
start_time = times[0][1] - times[0][0] + 1

for i in range(1,N):
    time,end_time = times[i]

    if end_time < start_time:
        start_time = end_time - time + 1
    else:
        end_time = start_time - 1
        start_time = end_time - time + 1

if start_time < 1:
    print(-1)
else:
    print(start_time - 1)
