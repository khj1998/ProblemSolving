import sys
input = sys.stdin.readline

N = int(input())
INF = int(1e9)*3
ans = -INF
operations = str(input()).rstrip()
oper_num = N//2

def calculate(num1,oper,num2):
    if oper == '-':
        return num1 - num2
    elif oper == '+':
        return num1 + num2
    else:
        return num1 * num2

if N == 1:
    print(int(operations[0]))
else:
    for i in range(2 ** oper_num):
        stack = []
        is_used, is_valid = False, True
        bin_string = str(bin(i))[2:].zfill(oper_num)

        for index, c in enumerate(bin_string, start=1):
            index *= 2
            oper, num = operations[index - 1], operations[index]

            if c == '0':
                is_used = False

                if not stack:
                    stack.append(operations[0])
                stack.append(oper)
                stack.append(num)
            elif c == '1' and not is_used:
                is_used = True

                if not stack:
                    stack.append(calculate(int(operations[0]),oper,int(num)))
                else:
                    last_num = int(stack.pop())
                    stack.append(calculate(last_num,oper,int(num)))
            elif c == '1' and is_used:
                is_valid = False
                break

        if is_valid:
            result = int(stack.pop(0))

            while stack:
                op = stack.pop(0)
                result = calculate(result,op,int(stack.pop(0)))

            ans = max(ans, result)

    print(ans)
