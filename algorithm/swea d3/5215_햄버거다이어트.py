def choose(k, s, c):
    global max_score
    if c > L:
        return
    if k == N:
        if s > max_score:
            max_score = s
        return

    choose(k+1, s + table[k][0], c + table[k][1])
    choose(k+1, s, c)

TC = int(input())
for tc in range(1, TC + 1):
    N, L = map(int,input().split())
    table = []
    for _ in range(N):
        table.append(list(map(int,input().split())))
    max_score = 0
    choose(0, 0, 0)
    print(f'#{tc} {max_score}')