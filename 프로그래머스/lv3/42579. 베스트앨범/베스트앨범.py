from collections import defaultdict

def solution(genres, plays):
    answer = []
    dic = defaultdict(list)
    genres_dic = {}
    
    for i in range(len(genres)):
        dic[genres[i]].append((plays[i],i))
        
        if genres[i] not in genres_dic.keys():
            genres_dic[genres[i]] = plays[i]
        else:
            genres_dic[genres[i]] += plays[i]
    
    genres_dic = sorted(genres_dic.items(),key = lambda x:-x[1])
    
    for genre in genres_dic:
        dic[genre[0]].sort(key = lambda x:(-x[0],x[1])) 
        
        for i in range(len(dic[genre[0]])):
            if i>1:
                break
            answer.append(dic[genre[0]][i][1])
    
    return answer