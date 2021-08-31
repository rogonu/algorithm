TC = int(input())
for tc in range(1, TC + 1 ):
    N , K = map(int, input().split())
    stu_hw = list(map(int, input().split()))
    student = list(range(1,N+1))
    for i in range(N):
        for j in range(K):
            if student[i] == stu_hw[j]:
                student[i] = 0
    print(f'#{tc}', end=' ')
    for l in range(N):
        if student[l] != 0:
            print(student[l], end=' ')
    print()
