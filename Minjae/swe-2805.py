T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    answer = 0
    value = []
    
    for i in range(N):
        inputs = list(map(int, list(input())))
        value.append(inputs)
    
    if N == 1:
        answer += value[0][0]
    else:
        medium = int(N/2)
        cnt = 0
        for i in range(medium + 1):
            for j in range(max(0, medium - cnt), min(N, medium + cnt + 1)):
                answer += value[i][j]
            cnt += 1

        cnt = 0
        for i in range(N - 1, medium, -1):
            for j in range(max(0, medium - cnt), min(N, medium + cnt + 1)):
                answer += value[i][j]
            cnt += 1

    print('#{} {}'.format(test_case, answer))