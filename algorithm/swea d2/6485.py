import sys
sys.stdin = open('input.txt', 'r')

#
#
# TC = int(input())
# for tc in range(1, TC + 1):
#     N = int(input())
#     A = []
#     B = []
#     C = []
#     for n in range(N):
#         a, b = map(int, input().split())
#         A.append(a)
#         B.append(b)
#     P = int(input())
#     for _ in range(P):
#         c = int(input())
#         C.append(c)
#     A_b = [0] * (P + 1)
#     B_b = [0] * (P + 1)
#     for i in range(N):
#         for j in range(1,P+ 1):
#             if A[i] == j:
#                 A_b[j] += 1
#             if B[i] == j:
#                 B_b[j] += 1
#     C.insert(0,0)
#     for k in range(1, P+1):
#         C[k] = C[k-1] + A_b[k] - B_b[k-1]
#     C.pop(0)
#
#     # print('#{} {}'.format(tc, ' '.join(map(str, C))))
#     print('#{}'.format(tc), end=' ')
#     print(*C)
TC = int(input())
for tc in range(1,TC + 1):
    N = int(input())
    A = [0] * 5001
    B = [0] * 5001
    C = [0] * 5001
    for _ in range(N):
        a, b = map(int, input().split())
        A[a] += 1
        B[b] += 1
    for i in range(1, len(C)):
        C[i] = C[i-1] +A[i] - B[i-1]
    P = int(input())
    print('#{}'.format(tc), end=' ')
    for j in range(P):
        c = int(input())
        print(C[c], end=' ')
    print()