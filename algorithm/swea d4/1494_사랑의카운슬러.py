TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    position = [list(map(int, input().split())) for _ in range(N)]
    vector_x = []
    vector_y = []
    for i in range(N - 1):
        for j in range(i+1, N):
            x_position = position[j][0] - position[i][0]
            y_position = position[j][1] - position[i][1]
            vector_x.append(x_position)
            vector_y.append(y_position)
    if len(vector_x) > 2:
        min_x = (vector_x[0] + vector_x[1]) ** 2
        min_y = (vector_y[0] + vector_y[1]) ** 2
    else:
        min_x = (vector_x[0]) ** 2
        min_y = (vector_y[0]) ** 2

    for m in range(len(vector_x) - 1):
        for n in range(m + 1, len(vector_x)):
            if (vector_x[m] + vector_x[n]) ** 2 < min_x:
                min_x = (vector_x[m] + vector_x[n]) ** 2
            if (vector_y[m] + vector_y[n]) ** 2 < min_y:
                min_y = (vector_y[m] + vector_y[n]) ** 2
    print(f'#{tc} {min_x + min_y}')