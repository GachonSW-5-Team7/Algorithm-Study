<<<<<<< HEAD
def solution(nums):
    
    import numpy as np
    from itertools import combinations
    
    def is_prime(x):
        for i in range(2,x):
            if x%i==0:
                return False
        return True
    
    combi=list(combinations(nums,3))
    answer=0
    
    for i in range (len(combi)):
        num=np.sum(combi[i])
        if is_prime(num):
            answer+=1
                
=======
def solution(nums):
    
    import numpy as np
    from itertools import combinations
    
    def is_prime(x):
        for i in range(2,x):
            if x%i==0:
                return False
        return True
    
    combi=list(combinations(nums,3))
    answer=0
    
    for i in range (len(combi)):
        num=np.sum(combi[i])
        if is_prime(num):
            answer+=1
                
>>>>>>> 43b43477f93417a27790e62dc22313fdb7dd94ca
    return answer