def solution(lottos, win_nums):
    ranking =[6,6,5,4,3,2,1]
    answer = [1,6]
    num_zero = lottos.count(0)
    count = 0
    
    if num_zero == 6:
        return answer
    else:
        for i in range(6):
            for j in range(6):
                if lottos[i] == 0:
                    continue
                elif lottos[i] == win_nums[j]:
                    count +=1
    
    answer[0] = ranking[count + num_zero]
    answer[1] = ranking[count]

    return answer