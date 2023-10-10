# 택배상자는 n이 증가하는 번호 순으로 있음.
def solution(order):
    answer = 0
    i = 1
    sub_belt = []
    
    while i != len(order) + 1:
        sub_belt.append(i)
        
        while sub_belt and sub_belt[-1] == order[answer]:
            sub_belt.pop()
            answer += 1
        
        i+=1
    
    return answer