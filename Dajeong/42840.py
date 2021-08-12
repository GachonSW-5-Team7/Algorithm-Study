def solution(answers):
    
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0] 
    result = []
    
    for i in range(len(answers)):
        j = i + 1
        if (j % 5 == 0) and (answers[i] == 5):
            score[0] += 1
        elif answers[i] == (j % 5):
            score[0] += 1
            
        if (j % 8 == 0) and (answers[i] == 5):
            score[1] += 1
        elif (answers[i] == p2[i % 8]):
            score[1] += 1
            
        if (j % 10 == 0) and (answers[i] == 5):
            score[2] += 1
        elif (answers[i] == p3[i % 10]):
            score[2] += 1
    
    for i in range(3):
        if(score[i] == max(score)):
            result.append(i+1)
            
    return result