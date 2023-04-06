def solution(sequence, k):
    answer = []
    length = len(sequence) -1
    start,end = 0,0
    now_sum = sequence[0]
    
    while True:
        if now_sum <= k:
            if now_sum == k:
                answer.append([start,end,end-start])
            end+=1
            if end>length:
                break
            now_sum += sequence[end]
        else:
            now_sum -= sequence[start]
            start+=1
            
    answer.sort(key=lambda x:(x[2],x[0]))
    ans = [answer[0][0],answer[0][1]]
    return ans