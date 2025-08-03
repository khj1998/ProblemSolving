# 증설해야하는 서버 수 : math.floor(이용자수/m)
import math

def solution(players, m, k):
    answer = 0
    now_server_num = [0 for _ in range(len(players))]
    
    def is_over_player(player_num,server_num):
        return (server_num + 1) * m <= player_num
    
    def calculate_increased_server_num(player_num,server_num) :
        need_server_num = math.floor(player_num/m)
        return need_server_num - server_num
    
    for i in range(len(players)):
        if is_over_player(players[i],now_server_num[i]):
            more_server = calculate_increased_server_num(players[i],now_server_num[i])
            answer += more_server
            
            for j in range(i,i + k):
                if j >= 24:
                    break
                now_server_num[j] += more_server
   
    return answer