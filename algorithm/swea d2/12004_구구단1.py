TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    res = 0
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if (N / i) in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            res += 1
    if res > 0:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')
