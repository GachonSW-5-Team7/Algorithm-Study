def solution(board, moves):
    answer = 0
    buffer=[]
    
    for i in range(0,len(moves)):
        for j in range(0,len(board)):
            if board[j][moves[i]-1]==0:
                continue
            else:
                if len(buffer)>0 and buffer[-1]==board[j][moves[i]-1]:
                    answer+=2
                    board[j][moves[i]-1]=0
                    del buffer[-1]
                    break
                else:
                    buffer.append(board[j][moves[i]-1])
                    board[j][moves[i]-1]=0
                    break

    return answer