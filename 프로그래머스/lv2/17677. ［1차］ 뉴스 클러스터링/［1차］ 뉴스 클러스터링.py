from collections import Counter

def solution(str1, str2):
    answer = 0
    s1,s2 = [],[]
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            s1.append((str1[i].lower()+str1[i+1].lower()))

    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            s2.append((str2[i].lower()+str2[i+1].lower()))
    
    if not s1 and not s2:
        return 65536
    
    S1 = Counter(s1)
    S2 = Counter(s2)
    
    inter = Counter(S1 & S2)
    union = Counter(S1 | S2)
    
    return (int)((len(list(inter.elements()))/len(list(union.elements())))*65536)