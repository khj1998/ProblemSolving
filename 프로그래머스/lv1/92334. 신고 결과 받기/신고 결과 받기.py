from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report_num = {}
    report_list = defaultdict(list)
    banned_user = []

    for id in id_list:
        report_num[id] = 0
        report_list[id].append("") 
    
    for rp in report:
        user,reported_user = rp.split()
        if reported_user not in report_list[user]:
            report_list[user].append(reported_user)
            report_num[reported_user] += 1 
    
    for key in report_num.keys():
        if report_num[key] >= k:
            banned_user.append(key)
    
    for id in id_list:
        mail = 0
        for reported_user in report_list[id]:
            if reported_user in banned_user:
                mail+=1
        answer.append(mail)
    
    return answer