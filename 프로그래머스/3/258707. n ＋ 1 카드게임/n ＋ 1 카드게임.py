def solution(coin, cards):
    n = len(cards)
    my_cards = set(cards[:n//3])
    pending_cards = set()
    round = 1
    target = len(cards) + 1
    deck_idx = n // 3
    
    while deck_idx < n:
        pending_cards.add(cards[deck_idx])
        pending_cards.add(cards[deck_idx+1])
        deck_idx += 2

        found_pair = False
        for card in list(my_cards):
            if target - card in my_cards:
                my_cards.remove(card)
                my_cards.remove(target - card)
                found_pair = True
                break
        if found_pair:
            round += 1
            continue

        if coin >= 1:
            for card in list(my_cards):
                if target - card in pending_cards:
                    my_cards.remove(card)
                    pending_cards.remove(target - card)
                    coin -= 1
                    found_pair = True
                    break
            if found_pair:
                round += 1
                continue
        
        if coin >= 2:
            for card in list(pending_cards):
                if target - card in pending_cards:
                    pending_cards.remove(card)
                    pending_cards.remove(target - card)
                    coin -= 2
                    found_pair = True
                    break
            if found_pair:
                round += 1
                continue
        break
        
    return round