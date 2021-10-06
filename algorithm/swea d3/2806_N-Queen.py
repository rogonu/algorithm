TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    Arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if Arr[i][j] == 0:
                Arr[i][j] = 0
                for 