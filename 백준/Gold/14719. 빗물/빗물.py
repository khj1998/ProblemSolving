from collections import deque
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    answer = 0
    border = 0
    H,W = map(int,input().split())
    block_height = list(map(int, input().split()))

    for i in range(1,len(block_height)-1):
        left_max = max(block_height[:i])
        right_max = max(block_height[i+1:])

        border = min(left_max,right_max)

        if block_height[i] < border:
            answer += (border - block_height[i])

    print(answer)