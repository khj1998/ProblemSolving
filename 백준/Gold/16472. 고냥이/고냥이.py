import sys
input = sys.stdin.readline

N = int(input())
s = str(input()).rstrip()
start,end = 0,0
dic = {}

ans = 1
dic[s[0]] = 1

while end < len(s)-1:
    temp = 0
    end += 1

    if s[end] not in dic.keys():
        dic[s[end]] = 1
    else:
        dic[s[end]] += 1

    if len(dic.keys()) <= N:
        for key in dic.keys():
            temp += dic[key]
        ans = max(ans,temp)
    else:
        while len(dic.keys()) > N:
            dic[s[start]] -= 1
            start += 1

            if dic[s[start-1]] == 0:
                dic.pop(s[start-1])

print(ans)
