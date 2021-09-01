import sys
sys.stdin = open('input.txt', 'r')
TC = int(input())
for tc in range(1, TC + 1):
    N, Q = map(int, input().split())
    box = [0] * (N+1)
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L,R+1):
            box[j] = i
    box.pop(0)
    print(f'#{tc}', end=' ')
    print(*box)