TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    wire_A = []
    wire_B = []
    #전선이 겹치는지 확인하기 위해 전선의 A와 B의 위치를 분리
    for _ in range(N):
        a, b = map(int, input().split())
        wire_A.append(a)
        wire_B.append(b)
    cnt = 0
    for n in range(N):
        for k in range(n+1, N):
            if wire_A[n] < wire_A[k]:
                if wire_B[n] > wire_B[k]:
                    cnt += 1
            elif wire_A[n] > wire_A[k]:
                if wire_B[n] < wire_B[k]:
                    cnt += 1
    print(f'#{tc} {cnt}')