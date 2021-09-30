
TC = int(input())
for tc in range(1, TC + 1):
    D, A, B, F = map(int, input().split())
    pos_A = 0
    pos_B = D
    pos_F = 0
    fly_direc = 1
    fly_distance = 0
    while pos_A < pos_B:
        if pos_F == pos_A:
            fly_direc = 1
        elif pos_F == pos_B:
            fly_direc = -1
        pos_F = fly_direc * F
        fly_distance += F
        pos_A += A
        pos_B -= B
    print('#{} {:.6f}'.format(tc,fly_distance))