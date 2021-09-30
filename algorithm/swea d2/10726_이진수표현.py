import sys
sys.stdin = open('input.txt', 'r')
TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    bin = ''
    while M > 0:
        rest = M % 2
        bin = str(rest) + bin
        M = M // 2

    a = bin[-N:]
    b = ''
    for i in range(N):
        b += '1'
    if a == b :
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')