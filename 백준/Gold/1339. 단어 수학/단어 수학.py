import sys
input=sys.stdin.readline

n=int(input())
alpha_dict={'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
alpha=[]
word_list=[]
max=9
ans=0

for _ in range(n):
    word=str(input()).rstrip()
    word_list.append(word)

for word in word_list:
    for i in range(len(word)):
        num=10**(len(word)-i-1)
        alpha_dict[word[i]]+=num

for num in alpha_dict.values():
    if num>0:
        alpha.append(num)

alpha.sort()
alpha.reverse()

for cost in alpha:
    ans+=cost*max
    max-=1

print(ans)