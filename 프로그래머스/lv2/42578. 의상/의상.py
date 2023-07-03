
def solution(clothes):
    answer = 1
    dic = {}
    
    for c,Type in clothes:
        if Type not in dic.keys():
            dic[Type] = 1
        else:
            dic[Type] += 1
    
    for i in dic.values():
        answer*=(i+1)
        
    return answer - 1