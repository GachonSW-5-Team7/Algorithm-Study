def solution(board, moves):
    answer = 0
    basket = []

    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i] - 1] != 0:
                basket.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                if len(basket) >= 2 and basket[-2] == basket[-1]:
                    answer += 2
                    del basket[-2]
                    del basket[-1]
                break        
            
    return answer