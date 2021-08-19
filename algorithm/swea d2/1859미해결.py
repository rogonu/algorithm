import sys
sys.stdin = open('input.txt', 'r')
def max_price():
    max_price = 0
    for i in range(N):
        if max_price < price[i]:
            max_price = price[i]
            max_pos = i
def gain():

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    price = list(map(int, input().split()))
    gain = 0
    max_price = 0
    for i in range(N):
        if max_price < price[i]:
            max_price = price[i]
            max_pos = i

        for j in range(1, N - i):
            if max_price < price[i+j]:
                max_price = price[i+j]
        gain += max_price - price[i]

    print(gain)
# test_cases = int(input())
#
# for t in range(1, test_cases + 1):
#     n = int(input())
#     prices = list(map(int, input().strip().split()))
#
#     result = 0
#     last_price = prices[-1]
#     for i in range(len(prices) - 1, -1, -1):
#         if last_price > prices[i]:
#             result += last_price - prices[i]
#         else:
#             last_price = prices[i]
#
#     print('#{} {}'.format(t, result))