# 각 숫자를 이진수로 표현하고, 빈 공간은 0으로 채워 넣는다.
# 루트 노드는 0일 수가 없다. 루트가 0인데 자식이 있다면 이진트리로 만들 수 없다.
def solution(numbers):
    answer = []
    
    def is_binary_tree(to_search_num):
        if len(to_search_num) == 1:
            return True
        
        l = len(to_search_num)
        mid_index = l//2
        mid = to_search_num[mid_index]
        
        left = to_search_num[:mid_index]
        right = to_search_num[mid_index+1:]
        
        if mid == '0' and ('1' in left or '1' in right):
            return False
        
        result_1 = is_binary_tree(left)
        result_2 = is_binary_tree(right)
        
        return result_1 and result_2

    def get_max_len(number):
        count = len(number)
        hight = 1
        
        while True:
            if 2**hight - 1 < count:
                hight += 1
                continue
            break
            
        return 2**hight - 1
        
    for number in numbers:
        num = bin(number)[2:]
        max_len = get_max_len(num)
        num = num.zfill(max_len)
        
        if is_binary_tree(num):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer
