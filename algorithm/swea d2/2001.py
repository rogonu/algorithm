import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    Arr = [list(map(int, input().split())) for _ in range(N)]
    max_v =0
    #몇번 내리치는지
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            #내리쳤을때 잡은 파리의 합
            for r in range(M):
                for c in range(M):
                    sum += Arr[i+r][j+c]
            if sum > max_v:
                max_v = sum
    print(f'#{tc} {max_v}')