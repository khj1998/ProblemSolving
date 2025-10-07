from collections import defaultdict

def solution(friends, gifts):
    answer = 0
    give_index = 0
    receive_index = 1

    friend_list = defaultdict(list)
    friend_gift = defaultdict(list)
    
    for a in friends:
        for b in friends:
            if a==b:
                continue
            friend_list[a].append([b,0])
            friend_gift[a] = [0,0]
            friend_gift[b] = [0,0]

    for gift in gifts:
        giver,receiver = gift.split(' ')
        
        for i in range(len(friend_list[giver])):
            r = friend_list[giver][i][0]
            
            if r == receiver:
                friend_list[giver][i][1] += 1
                break
        
        friend_gift[giver][give_index]+=1
        friend_gift[receiver][receive_index]+=1
    
    for giver in friend_list.keys():
        ans = 0
        
        for receiver,c in friend_list[giver]:
            giver_count = c
            for g,receiver_count in friend_list[receiver]:
                if g==giver:
                    if giver_count > receiver_count:
                        ans+=1
                    elif giver_count == receiver_count:
                        giver_index = friend_gift[giver][give_index] - friend_gift[giver][receive_index]
                        receiver_index = friend_gift[receiver][give_index] - friend_gift[receiver][receive_index]
                        if giver_index > receiver_index:
                            ans+=1
        answer = max(answer,ans)
    
    return answer