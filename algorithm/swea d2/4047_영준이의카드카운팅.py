TC = int(input())
for tc in range(1, TC + 1):
    S = input()
    space= []
    dia = []
    heart = []
    clover = []
    for i in range(0, len(S), 3):
        if S[i] == 'S':
            space.append(int(S[i+1]+S[i+2]))
        elif S[i] == 'D':
            dia.append(int(S[i+1]+S[i+2]))
        elif S[i] == 'H':
            heart.append(int(S[i+1]+S[i+2]))
        elif S[i] == 'C':
            clover.append(int(S[i + 1] + S[i + 2]))

    if len(space) == len(set(space)):
        res_s = 13 - len(space)
    else:
        res_s = 'ERROR'
    if len(dia) == len(set(dia)):
        res_d = 13 - len(dia)
    else:
        res_d = 'ERROR'
    if len(heart) == len(set(heart)):
        res_h = 13 - len(heart)
    else:
        res_h = 'ERROR'
    if len(clover) == len(set(clover)):
        res_c = 13 - len(clover)
    else:
        res_c = 'ERROR'
    if res_c == 'ERROR' or res_h == 'ERROR'or res_d == 'ERROR' or res_s == 'ERROR':
        print(f'#{tc} ERROR')
    else:
        print(f'#{tc} {res_s} {res_d} {res_h} {res_c}')

