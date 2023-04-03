def solution(name, yearning, photo):
    answer = []
    score_dic = {}
    
    for i in range(len(name)):
        score_dic[name[i]] = yearning[i]
    
    for p in photo:
        score = 0
        for n in p:
            if n not in score_dic.keys():
                continue
            score += score_dic[n]
        answer.append(score)
    
    return answer