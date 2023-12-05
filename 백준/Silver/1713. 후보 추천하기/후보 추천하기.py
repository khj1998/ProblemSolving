import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
recommend = []
idx = 0
voted_list = list(map(int,input().split()))

for i in range(K):
    is_find = False

    for j in range(len(recommend)):
        if recommend[j][2] == voted_list[i]:
            recommend[j][1] += 1
            is_find = True
            break

    if not is_find:
        if len(recommend) < N:
            recommend.append([idx, 1, voted_list[i]])
        else:
            recommend.pop(N-1)
            recommend.append([idx, 1, voted_list[i]])

    idx+=1
    recommend.sort(key = lambda x:(-x[1],-x[0]))

recommend.sort(key = lambda x:x[2])

for r in recommend:
    print(r[2],end= " ")