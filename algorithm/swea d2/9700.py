TC = int(input())
for tc in range(1, TC + 1):
    p, q = map(float, input().split())
    s1 =
    s2 = (1 - p * q) * (1 - (1 - p) * q) * p * q
    if s1 < s2:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
