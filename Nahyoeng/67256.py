def solution(numbers, hand):
    answer = ''                  
    
    num={'1':[-1,1],'2':[0,1],'3':[1,1],'4':[-1,0],'5':[0,0],'6':[1,0],'7':[-1,-1],'8':[0,-1],'9':[1,-1],'*':[-1,-2],'0':[0,-2],'#':[1,-2]}
    
    r=num["#"]
    l=num["*"]
    n=len(numbers)
    
    buffer=("".join(map(str,numbers)))
    
    for i in range(0,n):
        if buffer.startswith(("1","4","7")):
            answer+='L'
            l=num[buffer[0]]
            buffer=buffer[1:]
        elif buffer.startswith(("3","6","9")):
            answer+='R'
            r=num[buffer[0]]
            buffer=buffer[1:]
        else:
            ld=abs(l[0]-num[buffer[0]][0])+abs(l[1]-num[buffer[0]][1])
            rd=abs(r[0]-num[buffer[0]][0])+abs(r[1]-num[buffer[0]][1])
            
            if ld>rd:
                answer+='R'
                r=num[buffer[0]]
                buffer=buffer[1:]
            elif rd>ld:
                answer+='L'
                l=num[buffer[0]]
                buffer=buffer[1:]
            elif rd==ld:
                if hand=="right":
                    answer+='R'
                    r=num[buffer[0]]
                    buffer=buffer[1:]
                else:
                    answer+='L'
                    l=num[buffer[0]]
                    buffer=buffer[1:]
    
    return answer