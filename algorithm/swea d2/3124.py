TC = int(input())
for tc in range(1, TC + 1):
    n, m = map(int, input().split())
    uni = m * 2 - n
    twin = m - uni
    print(f'#{tc} {uni} {twin}')