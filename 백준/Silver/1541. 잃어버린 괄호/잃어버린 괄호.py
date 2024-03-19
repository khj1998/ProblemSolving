import sys
input=sys.stdin.readline

expression=input().split('-')
result=0

for i in range(len(expression)):
    expression[i]=expression[i].split('+')

for i in range(len(expression[0])):
    result+=int(expression[0][i])

for i in range(1,len(expression)):
    sum=0
    for j in range(len(expression[i])):
        sum+=int(expression[i][j])
    result-=sum

print(result)