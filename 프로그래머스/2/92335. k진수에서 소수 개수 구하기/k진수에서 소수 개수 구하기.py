import math

def solution(n, k):
    answer = 0
    
    def decimal_to_n(n,k):
        number = ''
        
        while n > 0:
            number = str(n%k) + number
            n = n//k
        
        return number
    
    convert_num = decimal_to_n(n,k).split('0')

    for num in convert_num:
        if len(num) == 0:
            continue
        if int(num) < 2:
            continue
        if int(num) == 2 or int(num) == 3:
            answer+=1
            continue
        num = int(num)
        
        is_prime = True
        
        for i in range(2,math.ceil(math.sqrt(num))+1):
            if num%i == 0:
                is_prime = False
                break
        
        if is_prime:
            answer += 1
            
    return answer