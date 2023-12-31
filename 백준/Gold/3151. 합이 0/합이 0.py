import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
ans = 0
array = list(map(int,input().split()))
array.sort()
counter = Counter(array)

for i in range(N-2):
    left,right = i+1,N-1

    while left < right:
        result = array[i] + array[left] + array[right]

        if result > 0:
            right-=1
        elif result < 0:
            left+=1
        else:
            # 코딩 실력 값이 같더라도 다른 인덱스라면 다른 팀
            if array[left] == array[right]:
                ans += (right-left)
            else:
                ans += counter[array[right]]

            left+=1

print(ans)
