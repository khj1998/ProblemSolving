def solution(array, commands):
    answer = []
    
    for command in commands:
        start,end,num = command
        temp = array[start-1:end]
        temp.sort()
        answer.append(temp[num-1])
    
    return answer