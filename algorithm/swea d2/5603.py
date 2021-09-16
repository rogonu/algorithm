TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    straw = []
    for _ in range(N):
        straw.append(int(input()))
    sum_straw = sum(straw)
    # for i in straw:
    #     sum_straw += i
    avg_straw = sum_straw//N
    res = 0
    for j in straw:
        if j < avg_straw:
            res += avg_straw-j
    print(f'#{tc} {res}')