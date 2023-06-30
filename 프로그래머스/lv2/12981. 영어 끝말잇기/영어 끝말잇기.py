def solution(n, words):
    answer = []
    words_list = []
    now_num = 1
    speak_cnt = 1
    is_end = False
    last_word = ''
    
    for word in words:
        if now_num > n:
            now_num = 1
            speak_cnt+=1
        
        if not words_list:
            last_word = word
            words_list.append(word)
        else:
            if word[0]==last_word[-1] and len(word)>1 and word not in words_list:
                last_word = word
                words_list.append(word)
            else:
                is_end = True
                break
        now_num+=1
    
    if not is_end:
        answer = [0,0]
    else:
        answer = [now_num,speak_cnt]
    return answer