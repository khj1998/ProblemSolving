def extract_today(t):
    t = t.split('.') 
    return int(t[0])*12*28 + int(t[1])*28 + int(t[2])

def solution(today, terms, privacies):
    answer = []
    term_length = {}
    today_date = extract_today(today)
    
    for term in terms:
        t,length = term.split(' ')
        term_length[t] = int(length)*28
    print(today_date)
    index=1
    
    for privacie in privacies:
        now = privacie[0:10].split(".")
        Type = privacie[-1]
        next_date = int(now[0])*12*28 + int(now[1])*28 + int(now[2]) + term_length[Type]-1
        
        if next_date < today_date:
            answer.append(index)
        
        index+=1
    return answer