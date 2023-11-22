def solution(n, k, cmd):
    answer = ['O']*n
    cur = k
    linked_list = {i:[i-1,i+1] for i in range(n)}
    del_node = []
    
    for c in cmd:
        Prev,Next = linked_list[cur]
        
        if len(c) == 1:
            if c == "C":
                answer[cur] = 'X'
                del_node.append((Prev,cur,Next))
                
                if Prev == -1:
                    linked_list[Next][0] = -1
                    cur = Next
                elif Next == n:
                    linked_list[Prev][1] = n
                    cur = Prev
                else:
                    linked_list[Prev][1] = Next
                    linked_list[Next][0] = Prev
                    cur = Next
            else: # 가장 최근 삭제한 인덱스 복구
                p,c,temp_n = del_node.pop()
                answer[c] = 'O'
                
                if p == -1:
                    linked_list[temp_n][0] = c
                elif temp_n == n:
                    linked_list[p][1] = c
                else:
                    linked_list[p][1] = c
                    linked_list[temp_n][0] = c
        else:
            op,num = c.split()
            num = int(num)
            
            if op == "D":
                for _ in range(num):
                    cur = linked_list[cur][1]
            if op == "U":
                for _ in range(num):
                    cur = linked_list[cur][0]
    
    return ''.join(answer)