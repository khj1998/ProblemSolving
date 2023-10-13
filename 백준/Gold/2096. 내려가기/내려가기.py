import sys
input = sys.stdin.readline

if __name__ == '__main__':
    max_ans,min_ans = [0,0,0],[0,0,0]
    N = int(input())

    for _ in range(N):
        a,b,c = list(map(int,input().split()))
        max_tmp, min_tmp = [0, 0, 0], [0, 0, 0]

        for i in range(3):
            if i==0:
                max_tmp[i] = a + max(max_ans[i],max_ans[i+1])
                min_tmp[i] = a + min(min_ans[i],min_ans[i+1])
            elif i==1:
                max_tmp[i] = b + max(max_ans[i-1],max_ans[i],max_ans[i+1])
                min_tmp[i] = b + min(min_ans[i-1],min_ans[i],min_ans[i+1])
            else:
                max_tmp[i] = c + max(max_ans[i-1],max_ans[i])
                min_tmp[i] = c + min(min_ans[i-1],min_ans[i])

            if i==2:
                max_ans = max_tmp
                min_ans = min_tmp

    print(max(max_ans),min(min_ans))