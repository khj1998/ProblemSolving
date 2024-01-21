import sys
input = sys.stdin.readline
from bisect import bisect_left,insort

N,M,K = map(int,input().split())
dic = {}
key_list = []

for _ in range(N):
    k,v = map(int,input().split())
    dic[k] = v
    insort(key_list,k)

def binary_search(x):
    index = bisect_left(key_list,x)

    if index == 0:
        if abs(key_list[index] - x) <= K:
            return index
    elif index == len(key_list):
        if abs(key_list[len(key_list)-1]-x) <= K:
            return len(key_list) - 1
    else:
        l_idx_value,r_idx_value = x- key_list[index-1],key_list[index]-x

        if l_idx_value<=K and l_idx_value < r_idx_value:
            return index-1
        elif r_idx_value<=K and l_idx_value > r_idx_value:
            return index
        elif l_idx_value<=K and l_idx_value == r_idx_value:
            return -2

    return -1

for _ in range(M):
    oper = list(map(int,input().split()))

    if oper[0] == 1:
        dic[oper[1]] = oper[2]
        insort(key_list,oper[1])
    elif oper[0] == 2:
        if oper[1] in dic:
            dic[oper[1]] = oper[2]
        else:
            index = binary_search(oper[1])
            if key_list and index != -1 and index != -2:
                dic[key_list[index]] = oper[2]
    else:
        if oper[1] in dic:
            print(dic[oper[1]])
        else:
            if not key_list:
                print(-1)
            else:
                index = binary_search(oper[1])

                if index == -2:
                    print('?')
                elif index == -1:
                    print(-1)
                else:
                    print(dic[key_list[index]])
