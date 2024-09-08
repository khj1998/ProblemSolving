import heapq

def solution(book_time):
    heap = []
    book_times = []
    
    for s,e in book_time:
        s = int(s[:2])*60 + int(s[3:])
        e = int(e[:2])*60 + int(e[3:])
        book_times.append([s,e])
    
    book_times.sort()
    
    for s,e in book_times:
        if not heap:
            heapq.heappush(heap,e)
            continue
        
        if s >= heap[0]+10:
            heapq.heappop(heap)
            
        heapq.heappush(heap,e)
    
    return len(heap)