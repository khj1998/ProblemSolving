import math

def solution(n):
    answer = 0
    check = [True]*(n+1)
    
    for i in range(2,int(math.sqrt(n))+1):
        j = 2
        
        while j*i <= n:
            check[i*j] = False
            j+=1
    
    for i in range(2,n+1):
        if check[i]:
            answer+=1
    
    return answer