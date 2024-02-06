import sys
input = sys.stdin.readline

circle_list = [[]]
ans = 0

for _ in range(4):
    circle_list.append(str(input()).rstrip())

for i in range(1,5):
    temp = []

    for j in range(8):
        if circle_list[i][j] == '1':
            temp.append(1)
        else:
            temp.append(0)

    circle_list[i] = temp

K = int(input())

# 방향 1 = 시계, 방향 -1 = 반시계
def rotate_circles(number,direct):
    check[number] = True
    temp_list = [0 for _ in range(8)]

    if direct == 1:
        temp_list[0] = circle_list[number][7]

        for i in range(1,8):
            temp_list[i] = circle_list[number][i-1]

        circle_list[number] = temp_list
    else:
        temp_list[7] = circle_list[number][0]

        for i in range(7):
            temp_list[i] = circle_list[number][i+1]

        circle_list[number] = temp_list

    if number-1 >= 1 and not check[number-1]:
        if left_right_list[number-1][1] != left_right_list[number][0]:
            rotate_circles(number-1,-direct)
    if number+1 <= 4 and not check[number+1]:
        if left_right_list[number+1][0] != left_right_list[number][1]:
            rotate_circles(number+1,-direct)

def get_circle_left_right():
    result = [[]]

    for i in range(1,5):
        temp = [circle_list[i][6],circle_list[i][2]]
        result.append(temp)

    return result

for _ in range(K):
    check = [False] * 5
    rotate_num, direct = map(int,input().split())
    left_right_list = get_circle_left_right()
    rotate_circles(rotate_num,direct)

for i in range(1,5):
    if circle_list[i][0] == 1:
        ans += (2**(i-1))

print(ans)
