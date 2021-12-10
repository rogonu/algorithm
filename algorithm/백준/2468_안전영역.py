di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
def flood(row, column, rain):
    St = []
    St.append((row, column))
    while St:
        row, column = St.pop()
        visited[row][column] = False
        for move in range(4):
            new_row = row + di[move]
            new_column = column + dj[move]
            if 0 <= new_row < N and 0 <= new_column < N and visited[new_row][new_column] and area[new_row][new_column] > rain:
                St.append((new_row, new_column))




N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
max_height = 0
for row in range(N):
    for column in range(N):
        if area[row][column] > max_height:
            max_height = area[row][column]
max_safety = 0
for rain in range(0, max_height+1):
    cnt = 0
    visited = [[True] * N for _ in range(N)]
    for row in range(N):
        for column in range(N):
            if area[row][column] > rain and visited[row][column]:
                flood(row, column, rain)
                cnt+= 1
    if max_safety < cnt:
        max_safety = cnt
print(max_safety)