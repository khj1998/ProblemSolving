import sys
input = sys.stdin.readline

if __name__ =="__main__":
    S = str(input()).rstrip()
    bomb = str(input()).rstrip()
    bomb_len = len(bomb)
    ans = []

    for i in range(len(S)):
        ans.append(S[i])
        if ''.join(ans[-bomb_len:]) == bomb:
            for _ in range(bomb_len):
                ans.pop()

    if len(ans) == 0:
        print("FRULA")
    else:
        print(''.join(ans))