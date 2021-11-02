TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    farm = [list(input()) for _ in range(N)]
    res = 0
    k = N // 2
    for i in range(k+1):
        for j in range(k-i, k+i+1):
            if i == k:
                res += int(farm[i][j])
            else:
                res += int(farm[i][j])
                res += int(farm[N-i-1][j])
    print(f'#{tc} {res}')
