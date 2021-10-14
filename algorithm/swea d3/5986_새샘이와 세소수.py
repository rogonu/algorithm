# def find_sosoo():
#     nums = set(range(2,1000))
#     notsosoo = set()
#     k = 2
#     while k < 1000:
#         for i in range(2, 1000):
#             if k!= i and k % i == 0:
#                 notsosoo.add(k)
#                 break
#         k += 1
#     res = sorted(list(nums-notsosoo))
#     return res
def make_primes(n):
    k = n + 1
    check = [True] * k
    check[0] = False
    check[1] = False
    m = int(k ** 0.5)
    for i in range(2, m + 1):
        if check[i]:
            for j in range(i + i, k, i):
                check[j] = False
    return [num for num in range(k) if check[num]]

def check(x, y, cnt):
    global  result
    if x > N:
        return
    if cnt == 3:
        if x == N:
            result += 1
        return

    for i in sosoo:
         if y <= i :

             check(x + i, i, cnt + 1)

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    sosoo = make_primes(N)
    result = 0
    check(0,0,0)
    print(f'#{tc} {result}')
