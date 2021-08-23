import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC + 1):
    Arr = [[''] * 15 for _ in range(5)]
    text = [list(map(str, input())) for _ in range(5)]
    for i in range(5):
        for j in range(len(text[i])):
            Arr[i][j] = text[i][j]
    print('#{}'.format(tc), end=' ')
    for i in range(15):
        for j in range(5):
            print(Arr[j][i], end='')
    print()
