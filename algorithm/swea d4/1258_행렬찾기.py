TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    Arr = [list(map(int, input().split())) for _ in range(N)]
    lst = []
    for i in range(N):
        for j in range(N):
            if Arr[i][j] != 0:
                rkfh = 0
                tpfh = 0
                new_i = i
                new_j = j
                while new_j < N and Arr[i][new_j] != 0 :
                    new_j += 1
                    rkfh += 1
                while new_i < N and Arr[new_i][j] != 0 :
                    new_i += 1
                    tpfh += 1
                lst.append((rkfh*tpfh,rkfh,tpfh))
                for r in range(tpfh):
                    for c in range(rkfh):
                        Arr[i + r][j + c] = 0

    # print(lst)
    lst.sort()
    # print(lst)
    for z in range(len(lst) - 1):
        if lst[z][0] == lst[z+1][0]:
            if lst[z][1] < lst[z+1][1]:
                lst[z], lst[z+1] = lst[z+1], lst[z]
    # print(lst)
    res = [len(lst)]
    for k in range(len(lst)):
        res.append(lst[k][2])
        res.append(lst[k][1])
    print(f'#{tc}', end=' ')
    print(*res)