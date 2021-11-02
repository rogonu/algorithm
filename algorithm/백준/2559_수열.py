N, K = map(int, input().split())
days = list(map(int, input().split()))


# for i in range(N - K + 1):
#     sum = 0
#     for j in range(i,i+K):
#         sum += days[j]
#     if max_sum < sum:
#         max_sum = sum


max_sum = sum(days[0:K])
sum_v = sum(days[0:K])
start = 0
end = K
for _ in range(N-K):
    sum_v = sum_v - days[start] + days[end]
    start += 1
    end += 1
    if max_sum < sum_v:
        max_sum = sum_v
print(max_sum)