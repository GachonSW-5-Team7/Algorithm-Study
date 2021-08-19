def solution(new_id):
    
    ##1단계
    new_id=new_id.lower() 
    id=""
    
    ##2단계
    for i in range(len(new_id)):
        if new_id[i]=="." or new_id[i]=="_" or new_id[i]=="-" or (96<ord(new_id[i])<123) or (47<ord(new_id[i])<58):
            id+=new_id[i]
    
    buffer=""
    
    ##3단계
    for i in range(len(id)):
        if i==0:
            buffer+=id[i]
        elif buffer[-1]==id[i] and id[i]=='.':
            i+=1
        else:
            buffer+=id[i]
    
    ##4단계
    if buffer[-1]=='.':
        buffer=buffer[:-1]
    if buffer and buffer[0]=='.':
        buffer=buffer[1:]
        
    
    ##5단계
    if not buffer:
        buffer+='a'
        
    ##6,7단계
    if len(buffer)>15:
        while(len(buffer)>15):
            buffer=buffer[:-1]
        if buffer[-1]=='.':
            buffer=buffer[:-1]
    elif len(buffer)<3:
        temp=buffer[-1]
        while(len(buffer)<3):
            buffer+=temp
                    
    answer = buffer
    return answer