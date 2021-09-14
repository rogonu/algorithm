def tiq(num1, num2):

    K = 1
    cnt = 0
    while  True:
        for k in range(1, K + 1):
            i = k
            j = K - k + 1
            cnt += 1
            if i == num1:
                if j == num2:
                    return cnt
        K += 1

def plus(x, y):
    new_x = x[0] + y[0]
    new_y = x[1] + y[1]
    return new_x, new_y
plus()
# def dosem(x):
#     cnt = 0
#     K = 1
#     while cnt < x:
#         for k in range(1, K + 1):
#             i = k
#             j = K - k + 1
#             cnt += 1
#             if cnt == x:
#                 break
#         K += 1
#     return (i, j)
print(tiq(3,3))