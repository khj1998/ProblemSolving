import sys

input = sys.stdin.readline
from collections import Counter

N = int(input())
K = int(input())
times = 0
x, y = 0, 0
snake_axis = [(0, 0)]
apples = []
now_direct = 0
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
directions = []

for _ in range(K):
    r, c = map(int, input().split())
    apples.append((r - 1, c - 1))

L = int(input())

for _ in range(L):
    X, C = map(str, input().split())
    directions.append((int(X), C))

while True:
    x, y = x + dx[now_direct], y + dy[now_direct]
    can_eat, is_collide = False, False

    times += 1

    # 벽에 부딪히는지 체크
    if not (0 <= x < N and 0 <= y < N):
        break

    for i in range(len(apples)):
        if apples[i][0] == x and apples[i][1] == y:
            can_eat = True
            apples.pop(i)
            break

    snake_axis.append((x, y))

    # 벰이 자신의 몸에 닿았는지 체크
    counter = Counter(snake_axis)

    for key in counter.keys():
        if counter[key] > 1:
            is_collide = True
            break

    if is_collide:
        break

    if not can_eat:
        snake_axis.pop(0)

    # 오른쪽 왼쪽 위쪽 아래쪽 0 1 2 3
    # L 왼쪽 90도 회전, D 오른쪽 90도 회전
    for i in range(L):
        if times == directions[i][0]:
            if now_direct == 0:
                if directions[i][1] == 'L':
                    now_direct = 2
                else:
                    now_direct = 3
            elif now_direct == 1:
                if directions[i][1] == 'L':
                    now_direct = 3
                else:
                    now_direct = 2
            elif now_direct == 2:
                if directions[i][1] == 'L':
                    now_direct = 1
                else:
                    now_direct = 0
            else:
                if directions[i][1] == 'L':
                    now_direct = 0
                else:
                    now_direct = 1

print(times)
