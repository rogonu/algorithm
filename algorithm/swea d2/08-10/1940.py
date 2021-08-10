import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = []
    for n in range(N):
        lst.append(list(map(int, input().split())))
        v = 0
        move = 0
        for i in lst:
            if i[0] == 0:
                v = v
            elif i[0] == 1:
                v += i[1]
            else:
                v -= i[1]
            if v < 0 :
                v = 0
            move += v
    print(f'#{tc} {move}')