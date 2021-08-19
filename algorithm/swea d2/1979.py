import sys
sys.stdin = open('input.txt', 'r')
# 미해결 했을 때 코드
# TC = int(input())
# for tc in range(1, TC+1):
#     N, K = map(int, input().split())
#     ARR = [list(map(int, input().split())) for _ in range(N)]
#     cnt = 0
#     result = 0
#     for i in range(N):
#         for j in range(N - K + 1):
#             if ARR[i][j] == 1:
#                 cnt += 1
#             elif cnt == K:
#                 result += 1
#     print(cnt)
def cnt_row():
    result = 0
    for i in range(N):
        cnt_r = 0
        for j in range(N):
            if Arr[i][j] == 1:
                cnt_r += 1
            else:
                cnt_r = 0
            if cnt_r == K:
                if j == N - 1:
                    result += 1
                elif Arr[i][j + 1] == 0:
                    result += 1
    return result
def cnt_column():
    result = 0
    for i in range(N):
        cnt_c = 0
        for j in range(N):
            if Arr[j][i] == 1:
                cnt_c += 1
            else:
                cnt_c = 0
            if cnt_c == K:
                if j == N - 1:
                    result += 1
                elif Arr[j+1][i] == 0:
                    result += 1
    return result
TC = int(input())

for tc in range(1, TC+1):
    N, K = map(int, input().split())
    Arr = [list(map(int, input().split())) for _ in range(N)]
    # result = 0
    # for i in range(N):
    #     cnt_r = 0
    #     for j in range(N):
    #         if Arr[i][j] == 1:
    #             cnt_r += 1
    #         else:
    #             cnt_r = 0
    #         if cnt_r == K:
    #             if j == N-1:
    #                 result += 1
    #             elif Arr[i][j+1] == 0:
    #                 result += 1
    #
    print(f'#{tc} {cnt_row()+cnt_column()}')