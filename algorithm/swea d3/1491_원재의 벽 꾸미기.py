TC = int(input())
for tc in range(1, TC + 1):
    N, A, B = map(int, input().split())

    min = 99999999999999999999999999
    for r in range(1, N):
        for c in range(1, N):
            if r * c > N:
                break
            if A * abs((r-c)) + B * (N - r * c) < min:
                min = A * abs((r-c)) + B * (N - r * c)
    print(f'#{tc} {min}')