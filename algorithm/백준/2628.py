import sys

sys.stdin = open('input.txt', 'r')

end_j, end_i = map(int, input().split())
n = int(input())
line_i = [0]
line_j = [0]
for _ in range(n):
    i, j = map(int, input().split())
    if i == 0:
        line_i.append(j)
    else:
        line_j.append(j)
line_i.append(end_i)
line_j.append(end_j)
line_i.sort()
line_j.sort()
max_i = 0
max_j = 0
for n in range(len(line_i) - 1):
    value_i = line_i[n + 1] - line_i[n]
    if value_i > max_i:
        max_i = value_i
for m in range(len(line_j) - 1):
    value_j = line_j[m + 1] - line_j[m]
    if value_j > max_j:
        max_j = value_j
print(max_i * max_j)
