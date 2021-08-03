cnt = int(input())

for i in range(cnt):
    n = int(input())

    if n % 2 == 1:
        k = -1 * (n//2) + n 
    else:
        k = -1 * (n//2)
    print(f'#{i+1} {k}')
    