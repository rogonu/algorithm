TC = int(input())
for tc in range (1, TC + 1):
    a, b, c = map(int,input().split())
    d = 0
    if a == b:
        d = c
    if a == c:
        d = b
    if b == c:
        d = a
    print('#{} {}'.format(tc, d))