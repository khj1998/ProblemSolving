def solution(s):
    answer = ''
    length = len(s)
    
    if length%2!=0:
        answer = s[(length-1)//2]
    else:
        start = (length-1)//2
        end = start+2
        answer = s[start:end]
    
    return answer