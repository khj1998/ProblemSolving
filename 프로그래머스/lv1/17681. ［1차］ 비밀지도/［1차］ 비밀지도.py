def solution(n, arr1, arr2):
    answer = []
    arr = list(zip(arr1,arr2))
    
    for a,b in arr:
        new_map = str(bin(a|b))[2:].rjust(n,'0')
        new_map = new_map.replace('1','#')
        new_map = new_map.replace('0',' ')
        answer.append(new_map)
    
    return answer