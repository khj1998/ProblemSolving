import sys
input = sys.stdin.readline

if __name__=="__main__":
    N,K = map(int,input().split())
    num = str(input()).rstrip()
    pop_count = 0
    stack = []

    for i in num:
        if not stack:
            stack.append(i)
        else:
            if int(i) <= int(stack[-1]):
                stack.append(i)
            else:
                now = int(i)
                while stack and pop_count < K:
                    if int(stack[-1]) >= now:
                        break
                    stack.pop()
                    pop_count += 1

                stack.append(i)

    while K-pop_count:
        stack.pop()
        pop_count+=1

    ans = ''.join(stack)
    print(int(ans))
