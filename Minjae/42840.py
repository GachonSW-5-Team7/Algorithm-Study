def solution(answers):
    answer = []
    
    oneans = [1, 2, 3, 4, 5]
    twoans = [2, 1, 2, 3, 2, 4, 2, 5]
    theans = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    passnum = [0, 0, 0]
    
    for i, val in enumerate(answers):
        if oneans[i % 5] == val:
            passnum[0] = passnum[0] + 1
        
        if twoans[i % 8] == val:
            passnum[1] = passnum[1] + 1
            
        if theans[i % 10] == val:
            passnum[2] = passnum[2] + 1

    maxnum = max(passnum)
    for i, val in enumerate(passnum):
        if val == maxnum:
            answer.append(i + 1)
            
    return answer