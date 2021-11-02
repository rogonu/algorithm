def soon(cnt):
    if cnt == N:
        a = soon_temp[:]
        soon_all.append(a)
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            soon_temp.append(i)
            soon(cnt + 1)
            visited[i] = False
            soon_temp.pop()

N = int(input())
visited = [False] * (N+1)
soon_all = []
soon_temp = []
soon(0)
for k in range(len(soon_all)):
    print(*soon_all[k])