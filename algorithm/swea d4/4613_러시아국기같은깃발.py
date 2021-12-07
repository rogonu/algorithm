def check(color):
    cnt_W = 0
    cnt_B = 0
    cnt_R = 0





TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    cnt = 0
    for white in flag[0]:
        if white != 'W':
            cnt += 1
    for red in flag[-1]:
        if red != 'R':
            cnt += 1
    res_flag = flag[1:-1]
    check(W)