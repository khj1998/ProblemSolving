def solution(players, callings):
    answer = []
    players_idx = {}
    num = len(players)
    
    for i in range(num):
        players_idx[players[i]] = i
    
    for name in callings:
        called_idx = players_idx[name]
        front_player = players[called_idx-1]
        
        players_idx[name] = called_idx-1
        players_idx[front_player] = called_idx
        
        players[called_idx-1] = name
        players[called_idx] = front_player
    
    return players