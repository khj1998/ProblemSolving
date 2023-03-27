def solution(book_time):
    answer = 0
    hotel_end = [-10]
    booktime = []
    
    for booking in book_time:
        start_time = int(booking[0][:2])*60 + int(booking[0][3:])
        end_time = int(booking[1][:2])*60 + int(booking[1][3:])
        booktime.append([start_time,end_time])
    booktime.sort()
    
    for start_time,end_time in booktime:
        available = False
        for i in range(len(hotel_end)):
            if hotel_end[i] + 10 <= start_time:
                hotel_end[i] = end_time
                available = True
                break
        
        if not available:
            hotel_end.append(end_time)
    
    answer = len(hotel_end)
    return answer