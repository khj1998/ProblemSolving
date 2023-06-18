def solution(board, moves):
    answer = 0
    stack = []
    height = len(board) 
    
    for move in moves:
        now_data = 0
        for row in range(height):
            now_data = board[row][move-1]
            if now_data != 0:
                board[row][move-1] = 0
                break
                
        if now_data!=0:
            if len(stack)>0 and stack[len(stack)-1]==now_data:
                stack.pop(len(stack)-1)
                answer+=2
            else:
                stack.append(now_data)
    return answer