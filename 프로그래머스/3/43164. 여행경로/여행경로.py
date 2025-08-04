def solution(tickets):
    airport_route = {}
    
    for start,end in tickets:
        if start not in airport_route:
            airport_route[start] = []
        airport_route[start].append(end)
        
        airport_route[start].sort()
    
    route = []
    print(airport_route)
    
    def dfs(start):
        while airport_route.get(start):
            next_route = airport_route[start].pop(0)
            dfs(next_route)
        route.append(start)    
    
    dfs("ICN")
    
    return route[::-1]