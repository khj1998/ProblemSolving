import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x]!=x:
        x = find_parent(parent,parent[x])
    return x

def union(parent,x,y):
    a = find_parent(parent,x)
    b = find_parent(parent,y)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ =="__main__":
    N = int(input())
    wires,edges = [],[]
    total_length = 0
    V = 0
    parent = [i for i in range(N+1)]

    for _ in range(N):
        wires.append(list(str(input().rstrip())))

    for i in range(N):
        for j in range(N):
            if wires[i][j] == '0':
                continue
            if wires[i][j].isupper():
                total_length += (ord(wires[i][j]) - 38)
                edges.append((ord(wires[i][j])-38,i+1,j+1))
            else:
                total_length += (ord(wires[i][j]) - 96)
                edges.append((ord(wires[i][j])-96,i+1,j+1))
    edges.sort()

    for length,x,y in edges:
        if find_parent(parent,x)!=find_parent(parent,y):
            total_length -= length
            union(parent,x,y)
            V+=1

        if V==N-1:
            break

    if V==N-1:
        print(total_length)
    else:
        print(-1)