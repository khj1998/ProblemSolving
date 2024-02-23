import sys
input = sys.stdin.readline

N,M = map(int,input().split())
ans = 0
paper = []

for _ in range(N):
    paper.append(str(input()).rstrip())

for i in range(1<<N*M):
    result = 0

    for row in range(N):
        temp = 0
        for col in range(M):
            index = M*row + col

            # 결과가 1이면 가로
            if (1<<index) & i:
                temp = temp*10 + int(paper[row][col])
            else:
                result += temp
                temp = 0
        result += temp

    for col in range(M):
        temp = 0
        for row in range(N):
            index = M*row + col

            if not ((1<<index) & i):
                temp = temp*10 + int(paper[row][col])
            else:
                result += temp
                temp = 0
        result += temp

    ans = max(ans,result)

print(ans)
