def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data,key = lambda x:(x[col-1],-x[0]))
    
    for i in range(row_begin-1,row_end):
        sum_data = 0
        for d in data[i]:
            sum_data += d%(i+1)
        
        answer = answer^sum_data
    
    return answer