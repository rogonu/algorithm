# import sys
#
# sys.stdin = open('input.txt', 'r')

TC = int(input())

for tc in range(1, TC + 1):
    p, q = map(int, input().split())
    def dosem(x):
        cnt = 0
        K = 1
        while cnt < x:
            for k in range(1, K + 1):
                i = k
                j = K - k + 1
                cnt += 1
                if cnt == x:
                    break
            K += 1
        return i, j


    def plus(x, y):
        new_x = x[0] + y[0]
        new_y = x[1] + y[1]
        return new_x, new_y


    def tiq(num1, num2):

        K = 1
        cnt = 0
        r = 0
        while r == 0:
            for k in range(1, K + 1):
                i = k
                j = K - k + 1
                cnt += 1
                # if i == num1:
                #     if j == num2:
                if i == num1 and j ==num2 :
                    return cnt
                        return cnt
            K += 1


    print(f'#{tc} {tiq(plus(dosem(p), dosem(q))[0], plus(dosem(p), dosem(q))[1])}')
