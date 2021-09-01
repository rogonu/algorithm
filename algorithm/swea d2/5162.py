TC = int(input())
for tc in range(1, TC +1):
    A, B, C = map(int, input().split())
    res = C // min(A, B)
    print(f'#{tc} {res}')