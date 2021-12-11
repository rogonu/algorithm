# N = int(input())
#
# infos = []
# for _ in range(N):
#     info = list(map(int, input().split()))
#     infos.append(info)
# max_length = 0
# for c in range(N):
#     lenth_1 = infos[c][0] + infos[c][2]
#     lenth_2 = infos[c][1] + infos[c][3]
#     max_length = max(max_length, lenth_1, lenth_2)
# Arr = [[0] * max_length for _ in range(max_length)]
# for i in range(N):
#     start_i = infos[i][0]
#     start_j = infos[i][1]
#     for m in range(infos[i][2]):
#         for n in range(infos[i][3]):
#             Arr[start_i + m][start_j + n] = i+1
# result= [0 for _ in range(N+1)]
# for row in range(max_length):
#     for column in range(max_length):
#         if Arr[row][column] in range(1,N+1):
#             result[Arr[row][column]] += 1
# for i in range(1, N+1):
#     print(result[i])


N = int(input())

infos = []
for _ in range(N):
    info = list(map(int, input().split()))
    infos.append(info)
max_length = 1001
result = [0]
for c in range(N):
    lenth_1 = infos[c][0] + infos[c][2]
    lenth_2 = infos[c][1] + infos[c][3]
    area = infos[c][2] * infos[c][3]
    result.append(area)
    # max_length = max(max_length, lenth_1, lenth_2)
Arr = [[0] * max_length for _ in range(max_length)]
for i in range(N):
    start_i = infos[i][0]
    start_j = infos[i][1]
    for m in range(infos[i][2]):
        for n in range(infos[i][3]):
            if Arr[start_i + m][start_j + n] in range(1,N+1):
                result[Arr[start_i + m][start_j + n]] -= 1
            Arr[start_i + m][start_j + n] = i+1

for i in range(1, N+1):
    print(result[i])
