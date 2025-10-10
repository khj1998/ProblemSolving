def solution(commands):
    merged = [[(r, c) for c in range(51)] for r in range(51)]
    board = [["" for _ in range(51)] for _ in range(51)]
    answer = []

    def find(r, c):
        if merged[r][c] == (r, c):
            return r, c
        pr, pc = merged[r][c]
        merged[r][c] = find(pr, pc)
        return merged[r][c]

    def union(r1, c1, r2, c2):
        pr1, pc1 = find(r1, c1)
        pr2, pc2 = find(r2, c2)

        if (pr1, pc1) == (pr2, pc2):
            return

        if board[pr1][pc1] != "":
            merged[pr2][pc2] = (pr1, pc1)
        else:
            merged[pr1][pc1] = (pr2, pc2)

    for command in commands:
        parts = command.split()
        cmd = parts[0]

        if cmd == "UPDATE":
            if len(parts) == 4: # UPDATE r c value
                r, c, value = int(parts[1]), int(parts[2]), parts[3]
                pr, pc = find(r, c)
                board[pr][pc] = value
            else: # UPDATE value1 value2
                value1, value2 = parts[1], parts[2]
                for r in range(1, 51):
                    for c in range(1, 51):
                        pr, pc = find(r, c)
                        if board[pr][pc] == value1:
                            board[pr][pc] = value2
        
        elif cmd == "MERGE":
            r1, c1, r2, c2 = map(int, parts[1:])
            # 자기 자신과 병합하는 경우는 무시
            if (r1, c1) != (r2, c2):
                union(r1, c1, r2, c2)

        elif cmd == "UNMERGE":
            r, c = map(int, parts[1:])
            pr, pc = find(r, c)
            # 부모 셀의 값을 기억
            value_to_keep = board[pr][pc]
            
            cells_to_unmerge = []
            # 같은 그룹에 속한 모든 셀을 찾음
            for i in range(1, 51):
                for j in range(1, 51):
                    if find(i, j) == (pr, pc):
                        cells_to_unmerge.append((i, j))
            
            # 찾은 셀들의 병합을 해제하고 값을 초기화
            for ur, uc in cells_to_unmerge:
                merged[ur][uc] = (ur, uc)
                board[ur][uc] = ""
            
            # 원래 (r, c) 셀에만 값을 다시 할당
            board[r][c] = value_to_keep

        elif cmd == "PRINT":
            r, c = map(int, parts[1:])
            pr, pc = find(r, c)
            value = board[pr][pc]
            if value == "":
                answer.append("EMPTY")
            else:
                answer.append(value)
                
    return answer