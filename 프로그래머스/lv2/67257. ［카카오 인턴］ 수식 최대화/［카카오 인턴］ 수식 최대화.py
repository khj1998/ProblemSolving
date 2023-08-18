from itertools import permutations

def solution(expression):
    answer = 0
    opers = list(permutations(['+','-','*'],3))
    
    for oper in opers:
        o1,o2 = oper[0],oper[1]
        result = []
        
        for e in expression.split(o1):
            temp = [f'({i})' for i in e.split(o2)]
            result.append(f"({o2.join(temp)})")
        answer = max(answer,abs(eval(o1.join(result))))
    
    return answer