# def soon(cnt):
#     if cnt == N:
#         a = soon_temp[:]
#         soon_all.append(a)
#         return
#
#     for i in range(1, N+1):
#         if not visited[i]:
#             visited[i] = True
#             soon_temp.append(i)
#             soon(cnt + 1)
#             visited[i] = False
#             soon_temp.pop()
#
# N = int(input())
# ques = list(map(int, input().split()))
# visited = [False] * (N+1)
# soon_all = []
# soon_temp = []
# soon(0)
# if ques[0] == 1:
#     print(*soon_all[ques[1]])
# else:
#     for k in range(len(soon_all)):
#         if soon_all[k] == ques[1:]:
#             print(k+1)


def soon_1(cnt):
    global k
    if k > ques[1]:
        return
    if cnt == N:
        k += 1
        if k == ques[1]:
            print(*soon_temp)


    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            soon_temp.append(i)
            soon_1(cnt + 1)
            visited[i] = False
            soon_temp.pop()

def soon_2(cnt):
    if cnt == N:
        if soon_temp == k:
            print(cnt)

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            soon_temp.append(i)
            soon_2(cnt + 1)
            visited[i] = False
            soon_temp.pop()

N = int(input())
ques = list(map(int, input().split()))
visited = [False] * (N+1)
soon_all = []
soon_temp = []
if ques[0] == 1:
    k = 0
    soon_1(0)
else:
    k = ques[1:]
    soon_2(0)