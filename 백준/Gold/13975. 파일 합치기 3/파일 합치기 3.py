import sys
input = sys.stdin.readline
import heapq

T = int(input())

for _ in range(T):
    N = int(input())
    ans = 0
    papers = list(map(int,input().split()))
    q = []

    for paper in papers:
        heapq.heappush(q,paper)

    while N >= 2:
        p1 = heapq.heappop(q)
        p2 = heapq.heappop(q)

        new_paper = p1+p2
        ans += new_paper
        heapq.heappush(q,new_paper)
        N-=1

    print(ans)
