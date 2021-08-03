T = int(input())
for i in range(1, T + 1):
    b = 0
    a = input()
    if a[:] == a[-1::-1]:
        b = 1

    print(f'#{i} {b}')
