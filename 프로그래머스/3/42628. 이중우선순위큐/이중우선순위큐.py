import heapq

def solution(operations):
    answer = []
    array = []
    
    for op in operations:
        oper,n = op.split(" ")
        
        if oper == 'I':
            heapq.heappush(array,int(n))
        elif oper == 'D' and len(array)>0:
            if int(n) == -1:
                heapq.heappop(array)
            else:
                array.pop(array.index(heapq.nlargest(1,array)[0]))

    if not array:
        return [0,0]
    else:
        return [max(array),min(array)]