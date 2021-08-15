def solution(new_id):
    answer = new_id

    # 1
    answer = answer.lower()

    # 2
    newans = ''
    for char in answer:
        if char.isalnum() or char == '-' or char == '_' or char == '.':
            newans += char

    answer = newans

    # 3
    while answer.find('..') != -1:
        answer = answer.replace('..', '.')

    # 4
    answer = answer.strip('.')

    # 5
    if len(answer) == 0:
        answer = 'a'

    # 6
    if len(answer) >= 16:
        answer = answer[:15].strip('.')

    # 7 
    if len(answer) <= 2:
        while len(answer) != 3:
            answer = answer + answer[len(answer) - 1]

    return answer