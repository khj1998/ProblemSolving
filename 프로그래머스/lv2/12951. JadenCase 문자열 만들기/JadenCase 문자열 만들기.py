def solution(s):
    answer = ''
    isStart = True
    asciis = []
    
    for i in range(65,91,1):
        asciis.append(i)
    for i in range(97,123,1):
        asciis.append(i)
    
    for c in s:
        if isStart and c!=' ':
            answer+=c.upper()
            isStart=False
        elif c!=' ':
            answer+=c.lower()
        else:
            answer+=c
            isStart=True
       
    return answer