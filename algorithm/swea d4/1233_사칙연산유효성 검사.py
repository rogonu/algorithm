sym = ['/', '-', '+', '*']
def solve(k):
    global res
    if soosick[k][1] in sym:  #노드에 있는게 연산기호일때
        if len(soosick[k]) == 4:
            solve(int(soosick[k][2]))
            solve(int(soosick[k][3]))
        else:
            res = 0
    else: #노드에 있는게 숫자일때
        if len(soosick[k]) > 2:
            res = 0

TC = 10
for tc in range(1, TC + 1):
    N = int(input())
    soosick = [[]]
    res = 1
    for i in range(1, N + 1):
        soosick.append(list(input().split()))

    solve(1)
    print(f'#{tc} {res}')