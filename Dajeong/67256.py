def solution(numbers, hand):
    answer = ''
    # Each finger starts from * and #
    # Convert them into int
    current = [10,12]
    
    # Convert zero into 11 since the numbers increase as buttons are below.
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 11
    
    # Answer
    for i in range(len(numbers)):
        if numbers[i] % 3 == 1:
            answer = answer + 'L'
            current[0] = numbers[i]
        elif numbers[i] // 3 > 0 and numbers[i] % 3 == 0:
            answer = answer + 'R'
            current[1] = numbers[i]
        else:
            disL = distance(current[0], numbers[i])
            disR = distance(current[1], numbers[i])
            if disL == disR:
                answer = answer + hand[0].upper()
                if hand == "left":
                    current[0] = numbers[i]
                else:
                    current[1] = numbers[i]
            elif disL > disR:
                answer = answer + 'R'
                current[1] = numbers[i]
            elif disL < disR:
                answer = answer + 'L'
                current[0] = numbers[i]

    return answer

def distance(cur_pos, next_pos):
    dis = 0
    gap = abs(next_pos - cur_pos)
    dis = dis + (gap // 3) + (gap % 3)
    
    return dis