def solution(lottos, win_nums):
    answer = []

    zero_count = lottos.count(0)
    is_set = set(lottos).intersection(set(win_nums))
    wincnt = [6, 6, 5, 4, 3, 2, 1]

    answer.append(wincnt[zero_count + len(is_set)])
    answer.append(wincnt[len(is_set)])

    return answer