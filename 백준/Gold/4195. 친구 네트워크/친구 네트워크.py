import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

T = int(input())

def find_parent(x):
    if friend_dic[x]!=x:
        friend_dic[x] = find_parent(friend_dic[x])
    return friend_dic[x]

def union(f1,f2):
    x = find_parent(f1)
    y = find_parent(f2)

    if x!=y:
        friend_dic[y] = x
        friend_number[x] += friend_number[y]
    print(friend_number[x])

for _ in range(T):
    F = int(input())
    friend_dic = {}
    friend_number = {}

    for _ in range(F):
        ans = 0
        f1,f2 = map(str,input().split())

        if f1 not in friend_dic.keys():
            friend_dic[f1] = f1
            friend_number[f1] = 1

        if f2 not in friend_dic.keys():
            friend_dic[f2] = f2
            friend_number[f2] = 1

        union(f1,f2)
