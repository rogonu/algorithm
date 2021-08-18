import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(N)]
    ts = []
    for i in range(N):
        total = 0
        for j in range(len(scores[i])):
            if j == 0:
                total += scores[i][j] * 35 / 100
            elif j == 1:
                total += scores[i][j] * 45 / 100
            else:
                total += scores[i][j] * 20 / 100
        ts.append(total)
    ks = ts[K-1]
    ts.sort(reverse=True)
    ts.index(ks)