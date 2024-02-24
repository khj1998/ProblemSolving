import sys
input = sys.stdin.readline

N = int(input())
INF = int(1e9)*3
ans = -INF
operations = str(input()).rstrip()
oper_num = N//2

if N == 1:
    print(int(operations[0]))
else:
    for i in range(2 ** oper_num):
        stack = []
        is_used, is_valid = False, True
        bin_string = str(bin(i))[2:].zfill(oper_num)

        for index, c in enumerate(bin_string, start=1):
            index *= 2
            oper, num, value = operations[index - 1], operations[index], 0

            if c == '0':
                is_used = False

                if not stack:
                    stack.append(operations[0])
                stack.append(oper)
                stack.append(num)
            elif c == '1' and not is_used:
                is_used = True

                if not stack:
                    if oper == '+':
                        value = int(operations[0]) + int(num)
                    elif oper == '-':
                        value = int(operations[0]) - int(num)
                    else:
                        value = int(operations[0]) * int(num)
                    stack.append(value)
                else:
                    last_num = int(stack.pop())
                    if oper == '+':
                        value = last_num + int(num)
                    elif oper == '-':
                        value = last_num - int(num)
                    else:
                        value = last_num * int(num)
                    stack.append(value)
            elif c == '1' and is_used:
                is_valid = False
                break

        if is_valid:
            result = int(stack.pop(0))

            while stack:
                op = stack.pop(0)

                if op == '+':
                    result += int(stack.pop(0))
                elif op == '-':
                    result -= int(stack.pop(0))
                elif op == '*':
                    result *= int(stack.pop(0))
            ans = max(ans, result)

    print(ans)
