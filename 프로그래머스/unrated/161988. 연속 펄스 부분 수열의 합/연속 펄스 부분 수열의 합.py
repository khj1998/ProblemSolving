def solution(sequence):
    answer = 0
    
    p1 = [1 for _ in range(len(sequence))]
    p2 = [1 for _ in range(len(sequence))]
    
    for i in range(0,len(sequence),2):
        p1[i]*=-1
    
    for i in range(1,len(sequence),2):
        p2[i]*=-1
        
    p1[0] = p1[0]*sequence[0]
    p2[0] = p2[0]*sequence[0]
    
    for i in range(1,len(sequence)):
        p1[i],p2[i] = p1[i]*sequence[i],p2[i]*sequence[i]
        
        if p1[i-1] >=0:
            p1[i] = p1[i] + p1[i-1]
        
        if p2[i-1] >=0:
            p2[i] = p2[i] + p2[i-1]
    
    return max(max(p1),max(p2))