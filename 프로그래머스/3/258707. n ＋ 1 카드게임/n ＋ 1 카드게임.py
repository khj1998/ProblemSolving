def solution(coin, cards):
    answer = 1
    n = len(cards)
    target = n+1
    now_index = n//3
    now_card_list = cards[:now_index]
    pending_card_list = []
    
    while now_index < n:
        flag = False
        pending_card_list.append(cards[now_index])
        pending_card_list.append(cards[now_index+1])
        
        now_index+=2
        
        for card in now_card_list:
            if (target - card) in now_card_list:
                now_card_list.remove(card)
                now_card_list.remove(target-card)
                flag = True
                break
            
        if not flag and coin >= 1:
            for card in now_card_list:
                if target - card in pending_card_list:
                    coin-=1
                    now_card_list.remove(card)
                    pending_card_list.remove(target-card)
                    flag = True
                    break
        
        if not flag and coin > 1:
            for card in pending_card_list:
                if target-card in pending_card_list:
                    coin-=2
                    pending_card_list.remove(card)
                    pending_card_list.remove(target-card)
                    flag = True
                    break
        
        if flag:
            answer+=1
            continue
        break
    return answer