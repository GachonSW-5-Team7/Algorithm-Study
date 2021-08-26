def solution(lottos, win_nums):
    
    import numpy as np
    
    min = len(set(lottos)&set(win_nums))
    max = min+lottos.count(0)
    
    if min==0:
        min+=1
    if max==0:
        max+=1
    
    answer = [7-max,7-min]
    return answer