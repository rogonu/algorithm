import sys
sys.stdin = open('input1961.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    ARR = [list(input().split()) for _ in range(N)]

    arr_90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_90[i][j] = ARR[N - 1 - j][i]

    arr_180 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_180[i][j] = ARR[N - 1 - i][N - 1 - j]

    arr_270 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_270[i][j] = ARR[j][N - 1 - i]
    print(f'#{tc}')
    for i in range(N):
        print(''.join(arr_90[i]), ''.join(arr_180[i]), ''.join(arr_270[i]))