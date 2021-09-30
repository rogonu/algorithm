TC = int(input())
for tc in range(1, TC + 1):
    D, L, N = map(int, input().split())
    cnt = 0
    total_damage = 0
    while cnt < N:
        next_damage = D* (1 + cnt * L / 100)
        total_damage += next_damage
        cnt += 1
    print(f'#{tc} {int(total_damage)}')