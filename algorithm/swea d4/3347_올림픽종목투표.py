TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    score = [0 for _ in range(N)]
    for i in range(M):
        max = 0
        for j in range(N):
            if Ai[j] <= Bi[i]:
                position = j
                break
        score[position] += 1
    max_2 = 0
    for k in range(N):
        if int(score[k]) > max_2:
            max_2 = int(score[k])
            position_2 = k
    print(f'#{tc} {position_2+1}')