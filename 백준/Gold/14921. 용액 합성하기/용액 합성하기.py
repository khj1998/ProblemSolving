import sys
input = sys.stdin.readline
INF = int(1e9)

if __name__ =="__main__":
    answer = INF
    ans = 0
    n = int(input())
    array = list(map(int,input().split()))
    array.sort()
    start = 0
    end = n-1

    while start<end:
        now = array[start]+array[end]
        if answer>abs(now):
            answer=abs(now)
            ans = array[start]+array[end]

        if now > 0:
            end-=1
        else:
            start+=1

    print(ans)