def solution(s):
    numlist = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(len(numlist)):
        s = s.replace(numlist[i], str(i))
        
    return int(s)