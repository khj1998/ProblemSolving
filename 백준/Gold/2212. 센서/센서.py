import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
ans = 0
array = list(map(int,input().split()))
array.sort()
stack = []

for i in range(N-1):
    stack.append(abs(array[i+1] - array[i]))

stack.sort()

for i in range(len(stack)-(K-1)):
    ans += stack[i]

print(ans)
