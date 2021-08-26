import sys

sys.stdin = open('input.txt', 'r')
N = int(input())
Arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(6):
    top = Arr[0][i]
    if i == 0:
        top = Arr[0][5]
    elif i == 1:
        top = Arr[0][3]
    elif i == 2:
        top = Arr[0][4]
    for j in range(6):
         = Arr[i][j]

for j in range(6):
    top = Arr[0][j]
    for i in range(6):
        for n in range(N):
            if Arr[1][i] == Arr[0][5]:
                bottom =