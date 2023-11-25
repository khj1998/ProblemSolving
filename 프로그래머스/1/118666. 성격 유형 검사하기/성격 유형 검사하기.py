from collections import defaultdict

def solution(survey, choices):
    ans_list = []
    types = ["RT","CF", "JM", "AN"]
    dic,score = defaultdict(list),{}
    
    for t in types:
        if t not in dic.keys():
            dic[t] = [0,0]
    
    for i in range(1,8):
        if i < 4:
            score[i] = 4-i
        else:
            score[i] = i-4
    
    for i in range(len(survey)):
        idx = 0 
                
        if choices[i] == 4:
            continue
            
        if choices[i] < 4: # 부정 => 첫번째 문자
            if ord(survey[i][0]) > ord(survey[i][1]):
                idx = 1
            temp = ''.join(sorted(survey[i]))
            dic[temp][idx] += score[choices[i]]
        else: # 긍정 => 두번째 문자
            if ord(survey[i][0]) < ord(survey[i][1]):
                idx = 1
            temp = ''.join(sorted(survey[i]))
            dic[temp][idx] += score[choices[i]]
            
    for key in dic.keys():
        if dic[key][0] < dic[key][1]:
            ans_list.append(key[1])
        else:
            ans_list.append(key[0])

    return ''.join(ans_list)