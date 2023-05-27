def solution(s, skip, index):
    answer = ''
    
    for c in s:
        c_ord = ord(c)
        cnt = 1
        
        while cnt<=index:
            c_ord +=1
            
            if c_ord > 122:
                c_ord = 97
                if chr(c_ord) in skip:
                    continue
                else:
                    cnt+=1
            else:
                if chr(c_ord) in skip:
                    continue
                else:
                    cnt+=1
        
        answer+=chr(c_ord)

    return answer