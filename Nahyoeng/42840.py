def solution(answers):
    
    student=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    score=[0,0,0]
    
    answer=[]
    
    for i in range(len(answers)):
        if answers[i]==student[0][i%5]:
            score[0]+=1
            
        if answers[i]==student[1][i%8]:
            score[1]+=1
            
        if answers[i]==student[2][i%10]:
            score[2]+=1
    
    best=max(score)
    res_list=list(filter(lambda x: score[x]==best,range(len(score))))

    if len(res_list)==1:
        if(res_list[0]==0):
            answer.append(1)
        elif(res_list[0]==1):
            answer.append(2)
        elif(res_list[0]==2):
            answer.append(3)
    else:
        answer=res_list
        answer.sort()
        
        for i in range(len(answer)):
            answer[i]+=1  
            
    return answer