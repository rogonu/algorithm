import sys
sys.stdin = open('input.txt', 'r')
TC = int(input())
for tc in range(1, TC + 1):
    N, P, T = map(int, input().split())
    min_v = 0
    max_v = 0
    if N > P + T:
        min_v = 0
    else:
        min_v = abs(P - T)
    if P < T:
        max_v = P
    else:
        max_v = T
    if N == P == T:
        max_v = N
        min_v = N
    print('#{} {} {}'.format(tc, max_v, min_v))
