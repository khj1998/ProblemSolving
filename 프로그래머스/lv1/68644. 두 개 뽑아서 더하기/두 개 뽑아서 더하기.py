def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            temp = numbers[i]+numbers[j]
            if temp not in answer:
                answer.append(temp)
    answer.sort()
    return answer