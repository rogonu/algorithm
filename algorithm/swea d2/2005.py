import sys
sys.stdin = open('input.txt', 'r')

TC =  int(input())
for tc in range(1, TC+1):
    N = int(input())
    Arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j or j == 0:
                Arr[i][j] = 1
            elif j > 0 and i > 0:
                Arr[i][j] = Arr[i-1][j] + Arr[i-1][j-1]
    for i in range(N):
        for j in range(N):
            if j > i:
                Arr[i][j] = ''
    print(f'#{tc}')
    for i in range(N):
        print(' '.join(map(str, Arr[i])))