import heapq

def solution(book_time):
    answer = 0
    real_book_time = []
    h = []
    
    for start,end in book_time:
        start_time = int(start[0:2])*60 + int(start[3:])
        end_time = int(end[0:2])*60 + int(end[3:])
        real_book_time.append((start_time,end_time))
        
    real_book_time.sort()
    
    for start_time,end_time in real_book_time:
        if not h:
            heapq.heappush(h,end_time)
            continue
        
        end = heapq.heappop(h)
        
        if start_time < end + 10:
            heapq.heappush(h,end_time)
            heapq.heappush(h,end)
        else:
            heapq.heappush(h,end_time)
    
    return len(h)