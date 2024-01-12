import sys
input = sys.stdin.readline
import heapq

T = int(input())

for _ in range(T):
    k = int(input())
    max_q,min_q = [],[]
    is_deleted = [False] * k

    for i in range(k):
        oper,n = map(str,input().split())

        if oper == 'I':
            heapq.heappush(max_q,(-int(n),i))
            heapq.heappush(min_q,(int(n),i))
        else:
            if n == '-1':
                while min_q and is_deleted[min_q[0][1]]:
                    heapq.heappop(min_q)

                if min_q:
                    n,idx = heapq.heappop(min_q)
                    is_deleted[idx] = True
            else:
                while max_q and is_deleted[max_q[0][1]]:
                    heapq.heappop(max_q)

                if max_q:
                    n, idx = heapq.heappop(max_q)
                    is_deleted[idx] = True

    while min_q and is_deleted[min_q[0][1]]:
        heapq.heappop(min_q)

    while max_q and is_deleted[max_q[0][1]]:
        heapq.heappop(max_q)

    if not min_q:
        print('EMPTY')
    else:
        print(-max_q[0][0],min_q[0][0])
