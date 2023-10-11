import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N,M = map(int,input().split())
    array = [0] + list(map(int,input().split()))

    for i in range(1,len(array)):
        array[i] += array[i-1]

    for _ in range(M):
        i,j = map(int,input().split())
        print(array[j]-array[i-1])