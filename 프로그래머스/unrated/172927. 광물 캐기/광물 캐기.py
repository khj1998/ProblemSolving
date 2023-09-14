def solution(picks, minerals):
    answer = 0
    idx = 0
    minerals = minerals[:sum(picks)*5]
    mineral_list = []
    
    while True:
        if idx+5 <= len(minerals):
            mineral_list.append(minerals[idx:idx+5])
            idx+=5
        else:
            mineral_list.append(minerals[idx:])
            break
    
    for i in mineral_list:
        dia,iron,stone = 0,0,0
        
        for j in i:
            if j == "diamond":
                dia+=1
            elif j == "iron":
                iron+=1
            else:
                stone+=1
        i += [dia,iron,stone]
    
    mineral_list.sort(key = lambda x:(-x[-3],-x[-2],-x[-1]))   
    
    for l in mineral_list:
        exp_list = [[0,0],[0,1],[0,2]]
        
        if sum(picks) == 0:
            break
        
        for i in range(len(l)-3):
            if picks[0]>0:
                exp_list[0][0] += 1
            if picks[1]>0:
                if l[i] == "diamond":
                    exp_list[1][0]+=5
                else:
                    exp_list[1][0]+=1
            if picks[2]>0:
                if l[i] == "diamond":
                    exp_list[2][0] += 25
                elif l[i] == "iron":
                    exp_list[2][0] += 5
                else:
                    exp_list[2][0] += 1
        
        exp_list.sort(key = lambda x:(x[0],-x[1]))
        
        for cost,idx in exp_list:
            if cost==0:
                continue
                    
            picks[idx] -= 1
            answer += cost
            break
    
    return answer