def solution(s):
    answer = 0
    start_ch = s[0]
    same = 1
    other = 0
    
    if len(s)==1:
        answer=1
    else:
        for i in range(1,len(s)):
            if s[i]!=start_ch:
                other+=1
            else:
                same+=1
            if same == other:
                answer+=1
                if i<len(s)-1:
                    same,other=0,0
                    start_ch = s[i+1]
            elif i==len(s)-1:
                answer+=1
    
    return answer