di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def find(i, j):
    global res
    if miro[i][j] == '3':
        res = 1
        return
    for d in range(4):
        new_i = i + di[d]
        new_j = j + dj[d]
        if miro[new_i][new_j] != '1' and not visited[new_i][new_j]:

            find(new_i, new_j)
            visited[new_i][new_j] = 1


TC = 10
for tc in range(1, TC + 1):
    N = int(input())
    miro = []
    res = 0
    visited = [[False] * 100 for _ in range(100)]
    for _ in range(100):
        miro.append(input())
    for i in range(100):
        for j in range(100):
            if miro[i][j] == '2':
                start_i = i
                start_j = j
    # visited[start_i][start_j]
    find(start_i,start_j)

    print(res)