import sys
sys.stdin = open('input1979.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    result = 0
    for i in range(N):
        for j in range(N - K + 1):
            if ARR[i][j] == 1:
                cnt += 1
            elif cnt == K:
                result += 1
    print(cnt)