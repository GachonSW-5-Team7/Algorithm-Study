T = int(input())

A = []
K = 0
answer = 0

def dfs(idx, value):
    global A, K, answer
    if idx == len(A):
        return
    elif value + A[idx] == K:
        answer += 1

    dfs(idx + 1, value)
    dfs(idx + 1, value + A[idx])
    
for test_case in range(1, T + 1):
    answer = 0
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    dfs(0, 0)

    print('#{} {}'.format(test_case, answer))