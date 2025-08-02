from collections import defaultdict
import math

def solution(fees, records):
    ans = []
    base_time = int(fees[0])
    base_fee = int(fees[1])
    unit_time = int(fees[2])
    unit_fee = int(fees[3])
    
    car_record = defaultdict(list)
    car_nums = set()
    
    for record in records:
        time,car_num,in_out = record.split(' ')
        car_record[car_num].append([in_out,time])
        car_nums.add(car_num)
    
    def calculate_total_times(last_start_time,end_time):
        if end_time == 'NONE':
            last_time = 23*60 +59
            start_time = int(last_start_time[0:2])*60 + int(last_start_time[3:])
            return last_time - start_time
        
        start_time = int(last_start_time[0:2])*60 + int(last_start_time[3:])
        end_time = int(end_time[0:2])*60 + int(end_time[3:])
        
        return end_time - start_time  
    
    def calculate_total_fees(total_times):
        if (total_times) <= base_time:
            return base_fee
        
        unit_time = int(fees[2])
        unit_fee = int(fees[3])
        additional_fee = math.ceil(((total_times - base_time) / unit_time)) * unit_fee
        
        return base_fee + additional_fee
    
    for car_num in car_nums:
        last_in_out = []
        last_start_time = ''
        total_times = 0
        
        for idx,(in_out,time) in enumerate(car_record[car_num],start = 0):
            if in_out == 'IN':
                if idx == len(car_record[car_num]) - 1:
                    total_times += calculate_total_times(time,'NONE')
                else:
                    last_start_time = time
                continue
            elif in_out == 'OUT':
                total_times += calculate_total_times(last_start_time,time)
        
        total_fees = calculate_total_fees(total_times)
        ans.append([car_num,total_fees])
    
    return [fee for car_num, fee in sorted(ans, key=lambda x: x[0])]