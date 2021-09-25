T = int(input())

def dfs(cur):
    global maxval, change, numboard, check

    
    if cur == change:
        maxval = max(int(''.join(map(str, numboard))), maxval)
        return

    for i in range(len(numboard)):
        for j in range(i + 1, len(numboard)):
            numboard[i], numboard[j] = numboard[j], numboard[i]
            num = int(''.join(map(str, numboard)))
            if not check.get((num, cur + 1), False):
                check[(num, cur + 1)] = True
                dfs(cur + 1)
            numboard[i], numboard[j] = numboard[j], numboard[i]


for test_case in range(1, T + 1):
    inputs = input().split(' ')
    numboard = list(map(int, list(inputs[0])))
    change = int(inputs[1])
    maxval = 0
    check = {}

    dfs(0)   

    print('#{} {}'.format(test_case, maxval))
