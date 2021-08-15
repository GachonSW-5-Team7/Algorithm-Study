def checkPrime(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True

def solution(nums):
    answer = {}
    
    for idx1, val1 in enumerate(nums):
        for idx2, val2, in enumerate(nums):
            if idx1 == idx2:
                continue
            
            for idx3, val3 in enumerate(nums):
                if idx1 == idx3 or idx2 == idx3:
                    continue
                
                valset = frozenset([val1, val2, val3])
                if not valset in answer.keys():
                    if checkPrime(val1 + val2 + val3):
                        answer[valset] = True
                    else:
                        answer[valset] = False
                
    return list(answer.values()).count(True)