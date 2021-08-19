def solution(new_id):
    
    # Step 1
    new_id.lower()
    
    # Step 2
    lst_id = list(new_id)
    lst_special_chr = list('~!@#$%^&*()=+[{]}:?,<>/')    
    
    for i in lst_special_chr:
        for j in lst_id:
            if i == j:
                lst_id.remove(j)
                
    # Step 3
    temp=[]
    for i in range(len(lst_id) - 1):
        if lst_id[i] == "." and lst_id[i + 1] == ".":
            temp.append(i)
                
    for j in temp:
        del lst_id[j]
        
    # Step 4
    
    if len(lst_id) == 1 and lst_id[0] == ".":
        lst_id = []
    elif len(lst_id) == 0:
        pass
    else:
        if lst_id[0] == "." and len(lst_id) != 0:
            del lst_id[0]
        
        if lst_id[len(lst_id) - 1] == "." and len(lst_id) != 0:
            del lst_id[len(lst_id) - 1]
    
    # Step 5
    if lst_id == []:
        lst_id.append('a')
        
    # Step 6
    if len(lst_id) >=16:
        del lst_id[16:]
        if lst_id[len(lst_id) - 1] == ".":
            del lst_id[len(lst_id) - 1]
            
    # Step 7
    if len(lst_id) == 1:
        lst_id = lst_id * 3
    elif len(lst_id) == 2:
        lst_id = lst_id * 2
        
    #print(lst_id)
    return "".join(lst_id)