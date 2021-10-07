import sys
sys.stdin = open('input.txt', 'r')
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    ships = []
    for _ in range(N):
        ships.append(int(input()))
    ships = ships[1:]
    cnt = 0


    while len(ships) > 0:
        wnrl = ships[0] - 1

        for i in ships[:]:
            if i % wnrl == 1:
                ships.remove(i)
        cnt += 1
    print(f'#{tc} {cnt}')



    # while sum(ships) > 1:
    #
    #     for j in range(1, len(ships)):
    #         if ships[j] != 0:
    #             wnrl = ships[j] -ships[0]
    #             break
    #
    #     for i in range(1, len(ships)):
    #         if ships[i] % wnrl == 1:
    #             ships[i] = 0
    #     cnt += 1
    # print(f'#{tc} {cnt}')