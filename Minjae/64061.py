def solution(board, moves):
    answer = 0
    basket = []
    
    for i in range(len(moves)):
        j = 0
        
        while j < len(board) - 1 and board[j][moves[i] - 1] == 0:
            j += 1

        if j == len(board) or board[j][moves[i] - 1] == 0:
            continue

        print('value', board[j][moves[i] - 1])
        
        if len(basket) >= 1:
            if basket[-1] == board[j][moves[i] - 1]:
                del basket[-1]
                answer += 2
            else:
                basket.append(board[j][moves[i] - 1])
        else:
            basket.append(board[j][moves[i] - 1])
            
        board[j][moves[i] - 1] = 0
        
    return answer