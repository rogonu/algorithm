dx = [-1, 1, 0, 0]
dy = [0, 0 ,-1, 1]


def find(x, y):
    cur_i = x
    cur_j = y
    for i in range(M):
        for j in range(N):
            for di in dx:
                new_i = cur_i + di
            for dj in dy:
                new_j = cur_j + dj

TC = int(input())
for tc in range(1, TC + 1):
    M, N, L = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(M)]
    find(0, 0)