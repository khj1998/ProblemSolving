def solution(number, k):
    answer = ''
    last_num = int(number[0])
    ans = []
    ans.append(number[0])
    
    for i in range(1,len(number)):
        while ans:
            if int(number[i]) > int(ans[-1]) and k>0:
                k-=1
                ans.pop()
            else:
                break
        
        ans.append(number[i])
    
    for _ in range(k):
        ans.pop()
    
    return ''.join(ans)