def check(x):
    a = 0
    for i in range(len(x)-1):
        if lst[i] > lst[i+1]:
            a += 1
    if a == 0:
        return len(x)
    else:
        return 0

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    boboon = [[]]
    for i in lst:
        size = len(boboon)
        for j in range(size):
            boboon.append(boboon[j] + [i])
    print(boboon)
    # print(len(boboon))
    res = []
    for k in range(len(boboon)):
        res.append(check(boboon[k]))
    print(res)


    # res = [0]
    # for i in range(N-1):
    #     if lst[i] < lst[i+1] and lst[i] > res[-1]:
    #         res.append(lst[i])
    # res.pop(0)
    # if lst[-1]>res[-1]:
    #     res.append(lst[-1])
    # print(f'#{tc} {len(res)}')