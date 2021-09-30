TC = int(input())
for tc in range(1, TC + 1):
    A, B = map(int, input().split())
    N = A/B
    if N == 1:
        res = 1
    else:
        res = N ** 2
    print(f'#{tc} {res}')