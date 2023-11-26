import sys
input = sys.stdin.readline

N = int(input())
ans_length = 0
answer = [[N]]
temp = [N]

def find_numbers(temp,num):
    idx = 0

    while True:
        if idx == 0:
            idx += 1
            temp.append(num)
            continue

        num = temp[idx-1] - temp[idx]

        if num < 0:
            break
        temp.append(num)
        idx+=1

    return temp,idx+1

for i in range(N,-1,-1):
    temp,length = find_numbers([N],i)

    if length > len(answer[0]):
        answer[0] = temp
        ans_length = length

print(ans_length)
for i in answer[0]:
    print(i,end=" ")