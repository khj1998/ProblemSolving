from collections import defaultdict

def solution(commands):
    answer = []
    sheet = [['']*51 for _ in range(51)]
    parent = [[] for _ in range(51)]
    group = defaultdict(list)
    
    for i in range(51):
        for j in range(51):
            parent[i].append([i,j])
            group[(i,j)] = [[i,j]]

    def find_parent(x,y):
        if parent[x][y] != [x,y]:
            parent[x][y] = find_parent(parent[x][y][0],parent[x][y][1])
        return parent[x][y]
    
    def union(x1,y1,x2,y2):
        if x1==x2 and y1==y2:
            return
        x1,y1 = find_parent(x1,y1)
        x2,y2 = find_parent(x2,y2)
        value1,value2 = sheet[x1][y1],sheet[x2][y2]
        
        if x1 <= x2:
            update(x1,y1,x2,y2,value1,value2)
        else:
            update(x2,y2,x1,y1,value1,value2)
    
    def update(px,py,x1,y1,value1,value2):
        if value1 != "":
            sheet[px][py] = value1
        elif value2 != "":
            sheet[px][py] = value2
        
        for x,y in group[(x1,y1)]:
            parent[x][y] = [px,py]
            group[(px,py)].append([x,y])
    
    for com in commands:
        com = com.split()
        
        if com[0] == "UPDATE":
            if len(com) == 4: # 자신이 속한 그룹이 있다면 모두 value로
                r,c = parent[int(com[1])][int(com[2])]
                sheet[r][c] = com[3]
            else: # value1을 가지고 있는 셀 모두 update
                for i in range(51):
                    for j in range(51):
                        r,c = parent[i][j]
                        if sheet[r][c] == com[1]:
                            sheet[r][c] = com[2]
        elif com[0] == "MERGE":
            r1,c1,r2,c2 = int(com[1]),int(com[2]),int(com[3]),int(com[4])
            if find_parent(r1,c1) != find_parent(r2,c2):
                union(r1,c1,r2,c2)
        elif com[0] == "UNMERGE":
            r,c = int(com[1]),int(com[2])
            pr,pc = find_parent(r,c)
            origin_val = sheet[pr][pc]
            
            for x,y in group[(pr,pc)]:
                if x==r and y==c:
                    sheet[x][y] = origin_val
                else:
                    sheet[x][y] = ''
                parent[x][y] = [x,y]
                group[(x,y)] = [[x,y]]
        elif com[0] == "PRINT": 
            r,c = int(com[1]),int(com[2])
            r,c = parent[r][c]
            
            if sheet[r][c] == '':
                answer.append("EMPTY")
            else:
                answer.append(sheet[r][c])

    return answer