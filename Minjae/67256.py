def solution(numbers, hand):
    left = [1, 4, 7, '*']
    right = [3, 6, 9, '#']
    middle = [2, 5, 8, 0]

    cur_left = '*'
    cur_right = '#'

    answer = ''
    for i in range(len(numbers)):
        if numbers[i] in left:
            cur_left = numbers[i]
            answer += 'L'
        elif numbers[i] in right:
            cur_right = numbers[i]
            answer += 'R'
        else:
            l_move, r_move = 0, 0
            l_temp, r_temp = cur_left, cur_right

            if cur_left in left:
                l_move += 1
                l_temp = middle[left.index(l_temp)]

            if cur_right in right:
                r_move += 1
                r_temp = middle[right.index(r_temp)]

            if l_temp != numbers[i]:
                l_move += abs(middle.index(numbers[i]) - middle.index(l_temp))

            if r_temp != numbers[i]:
                r_move += abs(middle.index(numbers[i]) - middle.index(r_temp))

            if l_move < r_move:
                answer += 'L'
                cur_left = numbers[i]
            elif r_move < l_move:
                answer += 'R'
                cur_right = numbers[i]
            else:
                if hand == 'left':
                    answer += 'L'
                    cur_left = numbers[i]
                else:
                    answer += 'R'
                    cur_right = numbers[i]

    return answer