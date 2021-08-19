def solution(nums):
    n = len(nums)
    result = 0
    
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if get_prime(nums[i]+nums[j]+nums[k]):
                    result +=1
    return result
        
def get_prime(num):
    state = 0
    
    for i in range(1,num):
        if (num % i) == 0 :
            state += 1
    
    if state == 1:
        return 1
    else:
        return 0