import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    D, H, M = map(int, input().split())
    res = 0
    if D == 11:
        if H < 11:
            res = -1
        elif H == 11:
            if M < 11:
                res= -1
            else:
                res = 60 * (H - 11) + (M - 11)
        else:
            res = 60*(H-11)+ (M-11)
    else:
        res = 24*60*(D-12)+(12*60)+49+60*H+M
    print(f'#{tc} {res}')