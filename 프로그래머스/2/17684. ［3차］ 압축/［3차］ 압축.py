def solution(msg):
    answer = []
    word_dict = {}
    
    for i in range(65,91):
        word_dict[chr(i)] = i - 64
    
    w = ''
    word_index = 27
    
    for c in msg:
        wc = w+c
        
        if wc in word_dict:
            w = wc
        else:
            answer.append(word_dict[w])
            word_dict[wc] = word_index
            word_index+=1
            w = c

    answer.append(word_dict[w])
            
    return answer