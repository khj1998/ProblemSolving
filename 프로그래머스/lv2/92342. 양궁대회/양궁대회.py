from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    score = [i for i in range(11)]
    arrows = list(combinations_with_replacement(score,n))
    
    for arrow in arrows:
        lion,apiche = 0,0
        temp = [0 for i in range(11)]
        
        for a in arrow:
            temp[a] += 1
        
        for i in range(10):
            if temp[i] > info[i]:
                lion += (10-i)
            elif info[i] > 0 and info[i] >= temp[i]:
                apiche += (10-i)
        
        if lion > apiche:
            temp.append(lion-apiche)
            answer.append(temp)
    
    if not answer:
        return [-1]
    else:
        answer.sort(key = lambda x:(-x[11],-x[10],-x[9],-x[8],-x[7],-x[6],-x[5],-x[4],-x[3],-x[2],-x[1],-x[0]))
        return answer[0][:11]