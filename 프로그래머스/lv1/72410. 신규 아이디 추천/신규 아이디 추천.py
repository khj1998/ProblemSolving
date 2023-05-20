def solution(new_id):
    answer = ''
    allow=['-','.','_']
    
    new_str = ''
    for i in range(len(new_id)):
        if ord(new_id[i])>=65 and ord(new_id[i])<=90:
            new_str += new_id[i].lower()
        else:
            new_str+=new_id[i]
    
    temp = ''
    for i in new_str:
        asci = ord(i)
        if 97<=asci<=122:
            temp += i
        elif 48<=asci<=57:
            temp += i
        elif i in allow:
            temp+=i
    new_str = temp
    
    duplicated = 0
    temp= ''
    for i in new_str:
        if duplicated:
            if i!='.':
                temp+=i
                duplicated=0
        else:
            if i=='.':
                duplicated = 1
            temp+=i
    
    print(temp)
    new_str = temp
    temp = ''
    for i in range(len(new_str)):
        if i == 0 and new_str[i]=='.':
            continue
        elif i == len(new_str)-1 and new_str[i]=='.':
            continue
        temp+=new_str[i]
    new_str = temp
    
    if len(new_str)==0:
        new_str = 'a'
    
    if len(new_str)>=16:
        new_str = new_str[:15]
        if new_str[14] == '.':
            new_str = new_str[:14]
    
    if len(new_str) <= 2:
        while len(new_str)!=3:
            new_str+=new_str[-1]
  
    return new_str