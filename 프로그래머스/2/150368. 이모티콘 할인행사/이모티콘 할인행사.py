# 목표 1. 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것. 2. 판매액  최대
# 사용자 구매 기준 1. 일정 비율 이상 할인하는 이모티콘을 모두 구매.
#2. 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입
from itertools import product

# 카카오 이모티콘 할인 총 경우의 수
# 각 경우의 수마다 모든 유저의 서비스 가입자, 총 판매액 계산
# 모든 유저의 서비스 가입자, 총 판매액 기준 sort

def solution(users, emoticons):
    answer=[]
    discount_list = list(product([10,20,30,40],repeat = len(emoticons)))
    
    for dis in discount_list:
        service_user = 0
        total_sale = 0
        
        for user in users:
            user_total_sale = 0
            dis_min,sale_min = user[0],user[1]
            
            for i in range(len(emoticons)):
                if dis[i] >= dis_min:
                    user_total_sale += ((100-dis[i])*emoticons[i])//100
            
            if user_total_sale >= sale_min:
                service_user+=1
            else:
                total_sale+=user_total_sale
        
        answer.append((service_user,total_sale))
    
    answer.sort(key = lambda x:(-x[0],-x[1]))
    
    return answer[0]