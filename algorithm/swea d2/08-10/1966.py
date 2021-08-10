import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(N-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    # result = " ".join(map(str, lst))
    for l in lst:
        print(f'#{tc} {l}', end=' ')
    print()

    # print(f'#{tc} {result}')