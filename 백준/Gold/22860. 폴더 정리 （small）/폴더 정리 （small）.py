import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import defaultdict

N,M = map(int,input().split())
folders = defaultdict(list)
is_folder = {}

def find_files(parent):
    if not folders[parent]:
        return

    for f in folders[parent]:
        if is_folder[f] == '0':
            files.append(f)
        else:
            find_files(f)

for _ in range(N+M):
    p,f,c= map(str,input().split())

    if p not in folders.keys():
        is_folder[p] = '1'
        folders[p] = [f]
    else:
        folders[p].append(f)

    if f not in is_folder.keys():
        is_folder[f] = c

Q = int(input())

for _ in range(Q):
    query = str(input()).rstrip()
    files = []
    temp = query.split("/")
    find_files(temp[-1])
    print(str(len(set(files))),str(len(files)))
