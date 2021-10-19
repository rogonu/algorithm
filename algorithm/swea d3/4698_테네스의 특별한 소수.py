nums = [False, False] + [True] * (10**6 - 1)
for i in range(2, 10**6 + 1):
    if nums[i]:
        for j in range(2 * i, 10 **6 + 1, i):
            nums[j] = False

TC = int(input())
for tc in range(1, TC + 1):
    D, A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B + 1):
        if nums[i] and str(D) in str(i):
            cnt += 1
    print(f'#{tc} {cnt}')

# TC = int(input())
# for tc in range(1, TC + 1):
#     D, A, B = map(int, input().split())
#     nums = [False, False] + [True] * (B -1)
#     primes = []
#     special_primes = []
#     for i in range(2, B + 1):
#         if nums[i]:
#             primes.append(i)
#             for j in range(2*i, B+1, i):
#                 nums[j] = False
#     for j in primes:
#         if j >= A:
#             cnt = 0
#             for k in str(j):
#                 if k == str(D):
#                     cnt += 1
#             if cnt > 0:
#                 special_primes.append(j)

#     print(f'#{tc} {len(special_primes)}')
