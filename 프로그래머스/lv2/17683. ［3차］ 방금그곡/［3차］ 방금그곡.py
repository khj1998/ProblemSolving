import math

def solution(m, musicinfos):
    answer = []
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    
    for musicinfo in musicinfos:
        temp = []
        start,end,title,info = musicinfo.split(',')
        start_time = int(start[:2])*60 + int(start[3:])
        end_time = int(end[:2])*60 + int(end[3:])
        
        info = info.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        l = len(info)
        now_idx = 0
        
        for _ in range(end_time-start_time):
            if now_idx == l-1:
                temp.append(info[now_idx])
                now_idx = 0
            else:
                temp.append(info[now_idx])
                now_idx += 1
            
        if m in ''.join(temp):
            answer.append((title,end_time-start_time))
    
    if answer:
        answer.sort(key = lambda x:-x[1])
        return answer[0][0]
    else:
        return '(None)'