import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int,input().split()))
array.sort()
ans = 0

if N < 3:
    print(0)
else:
    temp = []
    for i in range(N):
        now_num = array[i]
        start,end = 0,N-1

        if i == 0:
            start = 1
        if i == N-1:
            end = N-2

        while start < end:
            result = array[start] + array[end]

            if array[start] + array[end] < now_num:
                start += 1

                if start == i:
                    start+=1
            elif array[start] + array[end] > now_num:
                end -= 1

                if end == i:
                    end -= 1
            else:
                ans += 1
                break

    print(ans)
