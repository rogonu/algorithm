TC = int(input())
change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, TC+1):
    N = int(input())
    print(f'#{tc}')
    for i in change:
        if N // i > 0:
            print(N // i, end=' ')
            N = N % i
        else:
            print(0, end=' ')
    print()