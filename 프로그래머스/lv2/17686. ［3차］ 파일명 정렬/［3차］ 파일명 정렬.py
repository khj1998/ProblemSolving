def solution(files):
    answer = []
    temp = []
    
    for file in files:
        head,number,tail = '','',''
        is_number,is_tail = False,False
        
        for c in file:
            if c.isdigit() and not is_tail:
                number += c
                is_number = True
                is_head = False
            elif not is_number:
                head += c
            else:
                is_tail = True
                tail += c
        
        answer.append((head,number,tail))
        answer.sort(key =lambda x:(x[0].lower(),int(x[1])))
            
    return [''.join(word) for word in answer]