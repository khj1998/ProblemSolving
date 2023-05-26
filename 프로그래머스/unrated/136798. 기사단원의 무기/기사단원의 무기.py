import math

def solution(number, limit, power):
    answer = 0
    weights = []
    
    for num in range(1,number+1):
        ans=1
        for i in range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                ans+=1
                if i*i != num:
                    ans+=1

        if num>1:
            ans+=1
        weights.append(ans)
        
    for w in weights:
        if w>limit:
            answer+=power
        else:
            answer+=w
    return answer