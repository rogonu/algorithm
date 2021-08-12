import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    ARR = [list(map(int, input().split())) for _ in range(9)]
    result = 0

    # 행과 렬에서 찾기
    for i in range(9):
        a = []
        b = []
        for j in range(9):
            # 행찾기
            if ARR[i][j] not in a:
                a.append(ARR[i][j])
            # 렬찾기
            if ARR[j][i] not in b:
                b.append(ARR[j][i])
        if len(a) != 9 or len(b) != 9:
            result += 1

    # 3*3 씩 9칸 찾기
    for r in [0, 3, 6]:
        for c in [0, 3, 6]:
            lst = []
            for i in range(3):
                for j in range(3):
                    if ARR[r+i][c+j] not in lst:
                        lst.append(ARR[r+i][c+j])
            if len(lst) != 9:
                result += 1
            # print(lst)

    final = 0
    if result == 0:
        final += 1
    print(f'#{tc} {final}')