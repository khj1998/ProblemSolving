import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = str(input()).rstrip()
    left,right = 0,len(s)-1
    ans = 0

    while left < right:
        if s[left] == s[right]:
            left+=1
            right-=1
            continue

        else:
            left_split = s[left+1:right+1]
            right_split = s[left:right]

            if left_split[:] == left_split[::-1]:
                ans = 1
            elif right_split[:] == right_split[::-1]:
                ans = 1
            else:
                ans = 2
            break

    print(ans)
