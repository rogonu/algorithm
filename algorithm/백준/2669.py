import sys

sys.stdin = open('input.txt', 'r')

Arr = [[0] * 100 for _ in range(100)]
sum = 0
for _ in range(4):
    square = list(map(int, input().split()))
    for i in range(square[2] - square[0]):
        for j in range(square[3] - square[1]):
            if Arr[square[0] + i][square[1] + j] == 0:
                Arr[square[0] + i][square[1] + j] = 1
                sum += 1
print(sum)
