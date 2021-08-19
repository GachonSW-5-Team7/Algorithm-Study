def solution(scores):
    
    import numpy as np
    
    grade=0
    answer = ''
    
    scores=np.transpose(scores)
    
    for i in range(len(scores)):
        if max(scores[i])==scores[i][i]:
            res_list=list(filter(lambda x: scores[i][x]==max(scores[i]),range(len(scores[i]))))
            if len(res_list)==1:
                grade=(sum(scores[i])-scores[i][i])/(len(scores)-1)
            else:
                grade=sum(scores[i])/len(scores)
        elif min(scores[i])==scores[i][i]:
            res_list=list(filter(lambda x: scores[i][x]==min(scores[i]),range(len(scores[i]))))
            if len(res_list)==1:
                grade=(sum(scores[i])-scores[i][i])/(len(scores)-1)
            else:
                grade=sum(scores[i])/len(scores)
        else:
            grade=sum(scores[i])/len(scores)
            
        print(grade)
            
        if grade>=90:
            answer+='A'
        elif 90>grade>=80:
            answer+='B'
        elif 80>grade>=70:
            answer+='C'
        elif 70>grade>=50:
            answer+='D'
        elif 50>grade:
            answer+='F'       
    
    return answer