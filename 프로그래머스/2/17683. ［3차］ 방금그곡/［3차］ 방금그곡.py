# 정렬조건 - 재생된 시간이 제일 긴 제목, 먼저 입력된 제목
def solution(m, musicinfos):
    answer = []
    num = 0
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    
    for info in musicinfos:
        info = info.split(',')
        info[3] = info[3].replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        start,end = int(info[0][:2])*60 + int(info[0][3:]),int(info[1][:2])*60 + int(info[1][3:])
        
        l = len(info[3])
        temp = []
        
        for i in range(1,end-start+1):
            if i%l == 0:
                temp.append(info[3][-1])
            else:
                idx = (i%l) - 1
                temp.append(info[3][idx])

        if m in ''.join(temp):
            answer.append([end-start,num,info[2]])
            num+=1
    
    if not answer:
        return "(None)"
    
    answer.sort(key = lambda x:(-x[0],x[1]))
    return answer[0][2]