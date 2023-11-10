def solution(numbers):
    def check(num_bin,is_root_dummy):
        if len(num_bin)==1:
            return not is_root_dummy or num_bin[0]=="0"
        
        root_idx = len(num_bin)//2
        root = num_bin[root_idx]
        
        if root=="1" and is_root_dummy:
            return False
        
        return check(num_bin[:root_idx],root=="0") and check(num_bin[root_idx+1:],root=="0")
    
    answer = []
    node_num = 0
    
    for number in numbers:
        node_num = 1
        i = 1
        
        num_bin = bin(number)[2:]
        
        while node_num < len(num_bin):
            node_num += 2**i
            i+=1
            
        num_bin = (node_num-len(num_bin))*'0' + num_bin
        
        if check(num_bin,False):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer