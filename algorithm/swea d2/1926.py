N = int(input())
for i in range(1, N + 1):
    number = 0
    for j in str(i):
        if j in ['3', '6', '9']:
            number += 1
    if number == 0:
        print(i, end = ' ')
    else:
        print('-' * number, end=' ')