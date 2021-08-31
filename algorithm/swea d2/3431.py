TC = int(input())
for tc in range(1, TC + 1):
    L, U, X = map(int, input().split())
    result = 0
    if X > U:
        result = -1
    elif X < L :
        result = L - X


    print('#{} {}'.format(tc, result))