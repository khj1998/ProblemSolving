import sys
input = sys.stdin.readline
from collections import deque

S = int(input())
INF = int(1e9)
answer = [INF]*(S+1)
check = [[False]*(S+1) for _ in range(S+1)]
answer = [[INF]*(S+1) for _ in range(S+1)]
answer[1][0] = 0

q = deque()
q.append((1,0,0))

# i=0 화면에 붙여넣기, i=1 클립에 복사, i=2 화면에서 하나 삭제
while q:
    board,clip,time = q.popleft()
    check[board][clip] = True

    if board == S:
        break

    for i in range(3):
        if i == 0:
            if clip == 0 or clip + board > S:
                continue
            if not check[clip+board][clip] and time+1 < answer[board + clip][clip]:
                answer[board + clip][clip] = time + 1
                q.append((board+clip,clip,time+1))
        elif i == 1:
            if board == 0:
                continue
            q.append((board,board,time+1))
        elif i == 2:
            if board == 0:
                continue
            q.append((board-1,clip,time+1))

print(min(answer[S]))