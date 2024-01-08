import sys
input = sys.stdin.readline
from collections import defaultdict

buy_size = int(input())
m,n = map(int,input().split())
a_pizza,b_pizza = [],[]
a_pizze_dic,b_pizza_dic = defaultdict(int),defaultdict(int)
ans = 0

for _ in range(m):
    a_pizza.append(int(input()))

for _ in range(n):
    b_pizza.append(int(input()))

def get_slice_sum(size,pizze_list,dic):
    total_sum = sum(pizze_list)

    if total_sum not in dic.keys():
        dic[total_sum] = 1

    for i in range(size):
        count = pizze_list[i]
        dic[count] += 1

        for j in range(1,size-1):
            temp = pizze_list[(i+j)%(size)]
            count += temp
            dic[count] += 1

    dic[0] = 1

get_slice_sum(m,a_pizza,a_pizze_dic)
get_slice_sum(n,b_pizza,b_pizza_dic)

for a_key in a_pizze_dic.keys():
    ans += (a_pizze_dic[a_key] * b_pizza_dic[buy_size - a_key])

print(ans)
