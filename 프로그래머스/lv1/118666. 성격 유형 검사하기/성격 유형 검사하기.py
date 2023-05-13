# 1번 지표	라이언형(R), 튜브형(T)
# 2번 지표	콘형(C), 프로도형(F)
# 3번 지표	제이지형(J), 무지형(M)
# 4번 지표	어피치형(A), 네오형(N)

def solution(survey, choices):
    answer = ''
    types = []
    for i in range(1,5):
        if i==1:
            types.append([i,'R',0])
            types.append([i,'T',0])
        elif i==2:
            types.append([i,'C',0])
            types.append([i,'F',0])
        elif i==3:
            types.append([i,'J',0])
            types.append([i,'M',0])
        else:
            types.append([i,'A',0])
            types.append([i,'N',0])
    
    for i in range(len(survey)):
            s = survey[i]
            choice = choices[i]
            
            if choice < 4:
                s = s[0]
                for t in types:
                    if s in t:
                        if choice == 1:
                            t[2]+=3
                        elif choice == 2:
                            t[2]+=2
                        else:
                            t[2]+=1
                        break
            elif choice >= 5:
                s = s[1]
                for t in types:
                    if s in t:
                        if choice==5:
                            t[2] += 1
                        elif choice==6:
                            t[2] += 2
                        else:
                            t[2] += 3
    types.sort(key=lambda x:(x[0],-x[2],x[1]))
    
    start = 0
    
    while start <= 6:
        answer+=types[start][1]
        start+=2
    return answer