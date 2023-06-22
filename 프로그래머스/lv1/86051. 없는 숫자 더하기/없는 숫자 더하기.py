def solution(numbers):
    answer = 0
    num_list = [i for i in range(10)]
    
    for num in num_list:
        if num not in numbers:
            answer+=num
        
    return answer